import unittest

from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node
from engine.Simulator import Simulator


class SimulatorTest(unittest.TestCase):

    def test_Simulator(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                 ElectricNode("node2", 1, 1024, 500, []),
                 ElectricNode("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulator = Simulator(nodes, containers)
        simulator.simulate()

        self.assertEqual(Simulator.TIME_MAX_MINUTES, len(nodes[0].cpu_history))
        self.assertEqual(Simulator.TIME_MAX_MINUTES, len(nodes[0].memory_mb_history))
        self.assertEqual(Simulator.TIME_MAX_MINUTES, len(nodes[0].storage_mb_history))
        self.assertEqual(Simulator.TIME_MAX_MINUTES, len(nodes[0].green_energy_history))



if __name__ == '__main__':
    unittest.main()
