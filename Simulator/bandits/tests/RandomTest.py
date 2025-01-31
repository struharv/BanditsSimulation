import inspect
import random
import unittest

from parameterized import parameterized

from bandits.NewSimulator import NewSimulator
from bandits.tests.TestBase import TestBase


class RandomTest(TestBase):
    DECISION_EACH_SEC = 30

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_random(self, name, infrastructure):
        self.case_random(name, infrastructure)

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_random_1(self, name, infrastructure):
        self.case_random_1(name, infrastructure)

    def test_random_STATS_0(self):
        self.perform_stats("test_random_0", self.case_random, TestBase.TEST_SUITE)

    def test_random_STATS_1(self):
        self.perform_stats("test_random_1", self.case_random_1, TestBase.TEST_SUITE)

    def case_random(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: NewSimulator):
            if simulator.now() % RandomTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick,
                                inspect.currentframe().f_code.co_name, name, f"Random Reschedule - {name}")

        return results

    def case_random_1(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: NewSimulator):
            if simulator.now() % RandomTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick,
                                inspect.currentframe().f_code.co_name, name, f"Random Reschedule 1- {name}")

        return results

    """
    @parameterized.expand(JustTest.TEST_SUITE)
    def test_random_lowest_reward_first(self, name, infrastructure):
        nodes, containers = Infrastructure.make_infrastructure()

        def do_tick(simulator: NewSimulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                for container in containers:
                    pass

                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        self.do_simulation(nodes, containers, JustTest.random_init, do_tick, inspect.currentframe().f_code.co_name+"_"+name, f"Random Reschedule 1 - {name}")
    """

if __name__ == '__main__':
    unittest.main()
