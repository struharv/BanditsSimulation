import inspect
import unittest

from alessandro.LinUCBOrchestrator import LinUCBOrchestrator
from alessandro.LinUCBSimulator import LinUCBSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from visual.Visualizer import Visualizer


class LinUCB(unittest.TestCase):
    def test_something(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                 ElectricNode("node2", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                 ElectricNode("node3", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        orchestrator = LinUCBOrchestrator()

        simulatorUCB = LinUCBSimulator(nodes, containers)
        simulatorUCB.set_orchestrator(orchestrator)
        simulatorUCB.simulate()

        visualizer = Visualizer(simulatorUCB, inspect.currentframe().f_code.co_name)
        visualizer.draw()



