import inspect

from parameterized import parameterized

from _legacy.UCBBandit import UCBBandit
from bandits.tests.TestBase import TestBase



class UCBBanditTest(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_UCB_bandit(self, name, infrastructure):
        self.case_UCB_bandit(name, infrastructure)

    def test_UCB_bandit_STATS(self):
        self.perform_stats("test_UCB_bandit", self.case_UCB_bandit, TestBase.TEST_SUITE)

    def xtest_UCB_bandit_STATS1(self):
        self.perform_stats("test_UCB_bandit_1", self.case_UCB_bandit1, TestBase.TEST_SUITE)

    def xtest_UCB_bandit_STATS2(self):
        self.perform_stats("test_UCB_bandit_2", self.case_UCB_bandit2, TestBase.TEST_SUITE)

    def case_UCB_bandit(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit()
        result = self.simulate(nodes, containers, TestBase.random_init, None,
                               inspect.currentframe().f_code.co_name, name, f"UCB - {name}",
                               orchestrator=bandit)
        return result


    def case_UCB_bandit1(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit(alpha=0.4)
        result = self.simulate(nodes, containers, TestBase.random_init, None,
                               inspect.currentframe().f_code.co_name, name, f"UCB - {name}",
                               orchestrator=bandit)
        return result


    def case_UCB_bandit2(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit(alpha=0.6)
        result = self.simulate(nodes, containers, TestBase.random_init, None,
                               inspect.currentframe().f_code.co_name + "_" + name, f"UCB - {name}",
                               orchestrator=bandit)
        return result

