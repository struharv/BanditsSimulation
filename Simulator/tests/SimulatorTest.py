import unittest

from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node
from engine.Simulator import Simulator


class SimulatorTest(unittest.TestCase):

    def test_Simulator(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, [(7 * Simulator.HOUR_SECONDS, 0.0), (12 * Simulator.HOUR_SECONDS, 0.5), (14 * Simulator.HOUR_SECONDS, 0.5)]),
                 ElectricNode("node2", 1, 1024, 500, []),
                 ElectricNode("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulator = Simulator(nodes, containers)
        simulator.simulate()

        self.assertEqual(Simulator.TIME_MAX_SECONDS, len(nodes[0].cpu_history))
        self.assertEqual(Simulator.TIME_MAX_SECONDS, len(nodes[0].memory_mb_history))
        self.assertEqual(Simulator.TIME_MAX_SECONDS, len(nodes[0].storage_mb_history))
        self.assertEqual(Simulator.TIME_MAX_SECONDS, len(nodes[0].green_energy_history))

    def test_deploy_undeploy(self):
        nodes = [ElectricNode("node1", 1, 1024, 500, []),
                 ElectricNode("node2", 1, 1024, 500, []),
                 ElectricNode("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulator = Simulator(nodes, containers)

        self.assertIsNone(simulator.find_container_in_node("nonsence"))
        self.assertIsNone(simulator.find_container_in_node("container1"))

        self.assertIsNone(simulator.find_node("nonsence"))
        self.assertEqual(simulator.find_node("node1").name, "node1")

        self.assertIsNone(simulator.find_container("nonsence"))
        self.assertEqual(simulator.find_container("container1").name, "container1")


        # deploy undeploy
        simulator.find_node("node1").deploy(simulator.find_container("container1"))
        self.assertEqual(simulator.find_container_in_node("container1").name, "node1")
        self.assertTrue(simulator.find_node("node1").undeploy(simulator.find_container("container1").name))
        self.assertFalse(simulator.find_node("node1").undeploy(simulator.find_container("container1").name))
        self.assertIsNone(simulator.find_container_in_node("container1"))


        #migrate

        simulator.find_node("node1").deploy(simulator.find_container("container1"))
        simulator.find_node("node2").deploy(simulator.find_container("container2"))
        simulator.migrate("container1", "node3")
        simulator.migrate("container2", "node3")

        self.assertEqual(simulator.find_container_in_node("container1").name, "node3")
        self.assertEqual(simulator.find_container_in_node("container2").name, "node3")







if __name__ == '__main__':
    unittest.main()
