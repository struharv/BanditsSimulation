import inspect
import random
import unittest

from parameterized import parameterized

from alessandro.NewSimulator import NewSimulator
from alessandro.tests.test_helpers.Infrastructure import Infrastructure
from alessandro.tests.JustTest import JustTest



class HeuristicTest(JustTest):
    DECISION_EACH_SEC = 30

    @parameterized.expand(JustTest.TEST_SUITE)
    def test_random(self, name, infrastructure):
        self.case_random(name, infrastructure)


    def case_random(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: NewSimulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        results = self.do_simulation(nodes, containers, JustTest.random_init, do_tick,
                           inspect.currentframe().f_code.co_name + "_" + name, f"Random Reschedule - {name}")

        return results

    def test_random_STATS(self):
        self.do_test_stats("test_random", self.case_random, JustTest.TEST_SUITE)


    @parameterized.expand(JustTest.TEST_SUITE)
    def test_random_lowest_reward_first(self, name, infrastructure):
        nodes, containers = Infrastructure.make_infrastructure()

        def do_tick(simulator: NewSimulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                for container in containers:
                    pass

                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        self.do_simulation(nodes, containers, JustTest.random_init, do_tick, inspect.currentframe().f_code.co_name+"_"+name, f"Random Reschedule 1 - {name}")


if __name__ == '__main__':
    unittest.main()