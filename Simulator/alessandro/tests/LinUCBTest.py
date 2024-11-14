import inspect
import logging
import random
import unittest
from logging import Logger


from alessandro.LinUCBSimulator import LinUCBSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer


class LinUCB(unittest.TestCase):
    DECISION_EACH_SEC = 30

    def make_infrastructure(self):
        nodes = [ElectricNode("node1", 1, 1024, 500,
                              [(7 * Simulator.HOUR_SECONDS, 0.0), (12 * Simulator.HOUR_SECONDS, 0.5),
                               (14 * Simulator.HOUR_SECONDS, 0.5)]),
                 ElectricNode("node2", 1, 1024, 500,
                              [(7 * Simulator.HOUR_SECONDS, 0.0), (12 * Simulator.HOUR_SECONDS, 0.5),
                               (20 * Simulator.HOUR_SECONDS, 0.5)]),
                 ElectricNode("node3", 1, 1024, 500,
                              [(7 * Simulator.HOUR_SECONDS, 0.0), (12 * Simulator.HOUR_SECONDS, 0.5),
                               (23 * Simulator.HOUR_SECONDS, 0.5)])]

        containers = [Container("container1", 0.1, 256, 100),
                      Container("container2", 0.1, 256, 100),
                      Container("container3", 0.1, 256, 100),
                      Container("container4", 0.1, 256, 100),
                      Container("container5", 0.1, 256, 100),
                      Container("container6", 0.1, 256, 100),
                      ]

        return nodes, containers

    def do_simulation(self, nodes, containers, do_init, do_tick, test_name: str):
        simulatorUCB = LinUCBSimulator(nodes, containers)
        simulatorUCB.set_action_tick(do_tick)
        simulatorUCB.set_action_init(do_init)

        simulatorUCB.simulate()

        visualizer = Visualizer(simulatorUCB, test_name)
        visualizer.draw()

    def test_random(self):
        nodes, containers = self.make_infrastructure()

        def do_init(simulator: Simulator):
            pass

        def do_tick(simulator: Simulator):
            if simulator.now() % LinUCB.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name,  random.choice(nodes).name)

        self.do_simulation(nodes, containers, do_init, do_tick, inspect.currentframe().f_code.co_name)

    def test_random_lowest_reward_first(self):
        nodes, containers = self.make_infrastructure()

        def do_init(simulator: Simulator):
            cnt = 0
            buf_containers = []
            for cont in simulator.containers:
                buf_containers += [cont]

            while len(buf_containers) > 0:
                if simulator.migrate(buf_containers[0].name, random.choice(nodes).name):
                    del buf_containers[0]


        def do_tick(simulator: Simulator):
            if simulator.now() % LinUCB.DECISION_EACH_SEC == 0:
                #for container in containers:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        self.do_simulation(nodes, containers, do_tick, inspect.currentframe().f_code.co_name)
