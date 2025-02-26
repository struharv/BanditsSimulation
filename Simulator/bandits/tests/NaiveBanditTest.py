import inspect
import unittest

from parameterized import parameterized

from bandits.tests.TestBase import TestBase
from engine.bandits.MultiArmBandit import MultiArmBandit
from helpers.Permutations import Permutations


class NaiveBanditTest(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_naive_bandit(self, name, infrastructure):
        self.case_naive_bandit(name, infrastructure)

    def test_naive_bandit_STATS(self):
        self.perform_stats("test_naive_bandit", self.case_naive_bandit, TestBase.TEST_SUITE)

    def case_naive_bandit(self, name, infrastructure):
        nodes, containers = infrastructure

        permutations = Permutations(nodes, containers)
        permutations.print_permutations()
        sets = permutations.make_permutations()

        bandit = MultiArmBandit(sets)
        result = self.simulate(nodes, containers, None, None, inspect.currentframe().f_code.co_name, name,
                               f"Naive Bandit - {name}", orchestrator=bandit)
        return result


if __name__ == '__main__':
    unittest.main()


