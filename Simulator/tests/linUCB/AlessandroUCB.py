import unittest

from alessandro.LinUCBSimulator import LinUCBSimulator
from engine.Container import Container
from engine.Node import Node
from engine.Simulator import Simulator


class LinUCB(unittest.TestCase):
    def test_something(self):
        nodes = [Node("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                 Node("node2", 1, 1024, 500, []),
                 Node("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulatorUCB = LinUCBSimulator(nodes, containers)

        simulatorUCB.simulate()

        self.assertEqual(True, False)  # add assertion here

