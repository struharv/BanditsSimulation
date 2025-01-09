import inspect

from parameterized import parameterized

from alessandro.tests.JustTest import JustTest
from engine.bandits.UCBBandit import UCBBandit


class UCBBanditTest(JustTest):

    @parameterized.expand(JustTest.TEST_SUITE)
    def test_UCB_bandit(self, name, infrastructure):
        self.case_UCB_bandit(name, infrastructure)

    def test_UCB_bandit_STATS(self):
        self.perform_stats("test_UCB_bandit", self.case_UCB_bandit, JustTest.TEST_SUITE)

    def case_UCB_bandit(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit()
        result = self.simulate(nodes, containers, JustTest.random_init, None,
                               inspect.currentframe().f_code.co_name + "_" + name, f"UCB - {name}",
                               orchestrator=bandit)
        return result
