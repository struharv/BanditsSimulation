import inspect

from parameterized import parameterized

from bandits.UCBBandit3 import UCBBandit3
from bandits.tests.TestBase import TestBase



class UCBBandit3Test(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_UCB_bandit(self, name, infrastructure):
        self.case_UCB_bandit(name, infrastructure)

    def test_UCB_bandit_STATS(self):
        self.perform_stats("test_UCB_bandit", self.case_UCB_bandit, TestBase.TEST_SUITE)

    def case_UCB_bandit(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit3(len(nodes), len(nodes), alpha=0.1)
        result = self.simulate(nodes, containers, TestBase.random_init, None,
                               inspect.currentframe().f_code.co_name, name, f"UCB Multi Armed Bandit - {name}",
                               orchestrator=bandit)
        return result



