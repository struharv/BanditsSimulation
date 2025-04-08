import inspect
import random
import unittest

from parameterized import parameterized

from bandits.Simulator import Simulator
from bandits.tests.TestBase import TestBase
from bandits.tests.test_helpers.Infrastructure import Infrastructure
from electricitymaps.ElectricityMaps2 import ElectricityMap2Node
from engine.Container import Container
from engine.ElectricNode import ElectricNode

possible_deployments = None


def do_tick(simulator: Simulator):
    if simulator.now() % BestTest.DECISION_PERIOD_SEC == 0:

        best_Reward = None
        best_deployment = None
        for possible in possible_deployments:
            reward = simulator.compute_possible_reward(possible, simulator.time)
            if not best_Reward or reward >= best_Reward:
                best_Reward = reward
                best_deployment = possible

        # print(simulator.now(), best_Reward, best_deployment)
        simulator.deploy_as(best_deployment)


class BestTest(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_best(self, name, infrastructure):
        self.case_best(name, infrastructure)

    def test_best_bandit_STATS(self):
        self.perform_stats("test_best", self.case_best, TestBase.TEST_SUITE, explicit_repetitions=1)

    def case_best(self, name, infrastructure):
        global possible_deployments

        nodes, containers = infrastructure
        possible_deployments = self.compute_all_possible_deployments(nodes, containers)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick, inspect.currentframe().f_code.co_name, name, f"Best - {name}", perfmatrix=TestBase.PERFMATRIX)

        return results


    def test_UCBElMap_bandit(self, name= "best_elmmap"):
        self.case__UCBElMap_bandit(name)


    def case__UCBElMap_bandit(self, name):
        global possible_deployments

        days = 4
        nodes = [
            ElectricNode("nodeES", 1, 1024, 500, ElectricityMap2Node.toGreen("ES", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodePT", 1, 1024, 500, ElectricityMap2Node.toGreen("PT", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeUS", 1, 1024, 500,
                         ElectricityMap2Node.toGreen("US-NY-NYIS", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeFR", 1, 1024, 500, ElectricityMap2Node.toGreen("FR", 2024, 8, 20, limit=24 * days + 1)),
            ElectricNode("nodeHU", 1, 1024, 500, ElectricityMap2Node.toGreen("HU", 2024, 8, 20, limit=24 * days + 1))
            ]

        containers = [Container("container1", 0.1, 256, 10),
                      Container("container2", 0.1, 256, 10),
                      Container("container3", 0.1, 256, 10),
                      Container("container4", 0.1, 256, 10),
                      ]

        possible_deployments = self.compute_all_possible_deployments(nodes, containers)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick, inspect.currentframe().f_code.co_name, name, f"Best - {name}", simulation_time=24 * days * Simulator.HOUR_SECONDS)

        return results

    """
    def test_best_perfmatrix_big_spikey(self):
        name = "best_perfmat"
        infrastructure = Infrastructure.make_infrastructure_bigspikey()

        self.case_best_perf1(name, infrastructure)

    def case_best_perf1(self, name, infrastructure):
        global possible_deployments

        nodes, containers = infrastructure
        possible_deployments = self.compute_all_possible_deployments(nodes, containers)
        perfmatrix = TestBase.PERFMATRIX


        results = self.simulate(nodes, containers, TestBase.random_init, do_tick, inspect.currentframe().f_code.co_name, name, f"Best - {name}", perfmatrix=perfmatrix)

        return results
    """

if __name__ == '__main__':
    unittest.main()
