import inspect
import logging
import unittest
from logging import Logger

from alessandro.LinUCBOrchestrator import LinUCBOrchestrator
from alessandro.LinUCBSimulator import LinUCBSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer


class LinUCB(unittest.TestCase):
    def test_something(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, [(7 * 60 * 60, 0.0), (12 * 60 * 60, 0.5), (14 * 60 * 60 , 0.5)]),
                 ElectricNode("node2", 1, 1024, 500, [(7 * 60 * 60, 0.0), (12 * 60 * 60, 0.5), (14 * 60 * 60 , 0.5)]),
                 ElectricNode("node3", 1, 1024, 500, [(7 * 60 * 60, 0.0), (12 * 60 * 60 , 0.5), (14 * 60 * 60 , 0.5)])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]


        nodes[0].deploy(containers[0])
        nodes[1].deploy(containers[1])


        def do_tick(simulator: Simulator):
            logging.debug("custom do_tick")
            if simulator.now() %  10:
                pass


        orchestrator = LinUCBOrchestrator()

        simulatorUCB = LinUCBSimulator(nodes, containers)
        simulatorUCB.set_orchestrator(orchestrator)
        simulatorUCB.set_action_tick(do_tick)
        simulatorUCB.simulate()

        visualizer = Visualizer(simulatorUCB, inspect.currentframe().f_code.co_name)
        visualizer.draw()



