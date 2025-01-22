import inspect

from parameterized import parameterized

from bandits.tests.JustTest import TestBase
from engine.bandits.MultiArmBandit import MultiArmBandit


class NaiveBanditTestBase(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_naive_bandit(self, name, infrastructure):
        self.case_naive_bandit(name, infrastructure)

    def xtest_naive_bandit_STATS(self):
        self.perform_stats("test_naive_bandit", self.case_naive_bandit, TestBase.TEST_SUITE)

    def case_naive_bandit(self, name, infrastructure):
        nodes, containers = infrastructure

        sets = [
            [(nodes[0], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],
            [(nodes[1], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],
            [(nodes[2], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],

            [(nodes[0], [containers[0], containers[1]]), (nodes[1], [containers[2], containers[3], containers[4]])],
            [(nodes[1], [containers[0], containers[1]]), (nodes[0], [containers[2], containers[3], containers[4]])],

            [(nodes[1], [containers[0], containers[1]]), (nodes[2], [containers[2], containers[3], containers[4]])],
            [(nodes[2], [containers[0], containers[1]]), (nodes[1], [containers[2], containers[3], containers[4]])],

            [(nodes[0], [containers[0], containers[1]]), (nodes[2], [containers[2], containers[3], containers[4]])],
            [(nodes[2], [containers[0], containers[1]]), (nodes[0], [containers[2], containers[3], containers[4]])],

            [(nodes[0], [containers[0]]), (nodes[1], [containers[1], containers[2], containers[3], containers[4]])],
            [(nodes[1], [containers[0]]), (nodes[0], [containers[1], containers[2], containers[3], containers[4]])],

            [(nodes[0], [containers[0]]), (nodes[2], [containers[1], containers[2], containers[3], containers[4]])],
            [(nodes[2], [containers[0]]), (nodes[0], [containers[1], containers[2], containers[3], containers[4]])],

            # [(nodes[1], [containers[0]]), (nodes[2], [containers[1], containers[2], containers[3], containers[4]])],
            # [(nodes[2], [containers[0]]), (nodes[1], [containers[1], containers[2], containers[3], containers[4]])],

            # [(nodes[0], [containers[0]]), (nodes[1], [containers[1]]),
            #  (nodes[2], [containers[2], containers[3], containers[4]])],
            # [(nodes[0], [containers[1]]), (nodes[1], [containers[0]]),
            #  (nodes[2], [containers[2], containers[3], containers[4]])],

        ]

        bandit = MultiArmBandit(sets)
        result = self.simulate(nodes, containers, None, None, inspect.currentframe().f_code.co_name + "_" + name,
                               f"Naive Bandit - {name}", orchestrator=bandit)
        return result
