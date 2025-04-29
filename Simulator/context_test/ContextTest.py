import unittest

from context_test.ContextSimulator import ContextSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from bandits.Simulator import Simulator




class MyTestCase(unittest.TestCase):
    def test_something(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, []),
                 ElectricNode("node2", 1, 1024, 500, []),
                 ElectricNode("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.1, 256, 100),
                      Container("container2", 0.1, 256, 100)]

        simulator = Simulator(nodes, containers)

        context_sim = ContextSimulator(simulator)

        context_sim.learnx(len(nodes), len(nodes) * len(nodes[0].get_context(0)), 1.5)


if __name__ == '__main__':
    unittest.main()
