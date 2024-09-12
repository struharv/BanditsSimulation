import unittest

from engine.Container import Container
from engine.Node import Node
from engine.Simulator import Simulator


class SimulatorTest(unittest.TestCase):
    def test_Simulator(self):
        nodes = [Node("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                      Node("node2", 1, 1024, 500, []),
                      Node("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]


        simulator = Simulator(nodes, containers)
        simulator.simulate()


if __name__ == '__main__':
    unittest.main()
