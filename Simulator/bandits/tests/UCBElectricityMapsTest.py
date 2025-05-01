import inspect
import unittest

from parameterized import parameterized

from bandits.Simulator import Simulator
from bandits.Orchestrator import Orchestrator
from bandits.UCBBandit3 import UCBBandit3
from bandits.tests.TestBase import TestBase
from electricitymaps.ElectricityMaps2 import ElectricityMap2Node
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from visual.Visualizer import Visualizer


class ElectricityMapsTest(TestBase):

    def test_UCBElMap_bandit(self, name= "UCB_elmmap"):
        self.case__UCBElMap_bandit(name)


    def case__UCBElMap_bandit(self, name):
        days = 4
        nodes = [
            ElectricNode("nodeES", 1, 1024, 500, ElectricityMap2Node.toGreen("ES", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodePT", 1, 1024, 500, ElectricityMap2Node.toGreen("PT", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeUS", 1, 1024, 500,
                         ElectricityMap2Node.toGreen("US-NY-NYIS", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeFR", 1, 1024, 500, ElectricityMap2Node.toGreen("FR", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeHU", 1, 1024, 500, ElectricityMap2Node.toGreen("HU", 2024, 8, 20, limit=24 * days + 1))
            ]

        containers = []
        container_cpu = 0.15
        container_memory = 10
        container_storage = 10
        for i in range(10):
            containers += [Container(f"container{i}", container_cpu, container_memory, container_storage)]


        perfmatrix = TestBase.PERFMATRIX

        bandit = UCBBandit3(len(nodes), len(nodes) * len(nodes[0].get_context(0)), alpha=0.1)
        result = self.simulate(nodes, containers, TestBase.random_init, None,
                               inspect.currentframe().f_code.co_name, name, f"UCB Multi Armed Bandit - {name}",
                               simulation_time=24 * days * Simulator.HOUR_SECONDS, orchestrator=bandit)
        return result





if __name__ == '__main__':
    unittest.main()
