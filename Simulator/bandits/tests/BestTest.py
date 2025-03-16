import inspect
import random
import unittest

from parameterized import parameterized

from bandits.NewSimulator import NewSimulator
from bandits.tests.TestBase import TestBase


class BestTest(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_best(self, name, infrastructure):
        self.case_best(name, infrastructure)

    def test_best_bandit_STATS(self):
        self.perform_stats("test_best", self.case_best, TestBase.TEST_SUITE, explicit_repetitions=1)

    def case_best(self, name, infrastructure):
        nodes, containers = infrastructure
        possible_deployments = self.compute_all_possible_deployments(nodes, containers)

        def do_tick(simulator: NewSimulator):

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

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick, inspect.currentframe().f_code.co_name, name, f"Best - {name}")

        return results


if __name__ == '__main__':
    unittest.main()
