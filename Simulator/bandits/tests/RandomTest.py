import inspect
import random
import unittest

from parameterized import parameterized

from bandits.Simulator import Simulator
from bandits.tests.TestBase import TestBase


class RandomTest(TestBase):

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_random(self, name, infrastructure):
        self.case_random(name, infrastructure)

    def test_random_STATS_0(self):
        self.perform_stats("test_random_0", self.case_random, TestBase.TEST_SUITE)

    def case_random(self, name, infrastructure):
        nodes, containers, perfmatrix = infrastructure

        def do_tick(simulator: Simulator):
            if simulator.now() % RandomTest.DECISION_PERIOD_SEC == 0:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick,
                                inspect.currentframe().f_code.co_name, name, f"Random - {name}")

        return results


if __name__ == '__main__':
    unittest.main()
