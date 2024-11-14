import inspect
import logging
import random
import unittest
from logging import Logger


from alessandro.LinUCBSimulator import LinUCBSimulator
from alessandro.tests.Infrastructure import Infrastructure
from alessandro.tests.JustTest import JustTest
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer
from parameterized import parameterized



def random_init(simulator: Simulator):
    buf_containers = []
    for cont in simulator.containers:
        buf_containers += [cont]

    while len(buf_containers) > 0:
        if simulator.migrate(buf_containers[0].name, random.choice(simulator.nodes).name):
            del buf_containers[0]


class HeuristicTest(JustTest):
    DECISION_EACH_SEC = 30

    @parameterized.expand([
        ["foo", Infrastructure.make_infrastructure()],
        ["bar", Infrastructure.make_infrastructure()],
        ["lee", Infrastructure.make_infrastructure()],
    ])
    def test_random(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: Simulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name,  random.choice(nodes).name)

        self.do_simulation(nodes, containers, random_init, do_tick, inspect.currentframe().f_code.co_name+name)

    def test_random_lowest_reward_first(self):
        nodes, containers = Infrastructure.make_infrastructure()

        def do_tick(simulator: Simulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                for container in containers:
                    pass

                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        self.do_simulation(nodes, containers, random_init, do_tick, inspect.currentframe().f_code.co_name)

