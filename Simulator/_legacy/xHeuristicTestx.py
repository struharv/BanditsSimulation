import inspect
from random import random

from parameterized import parameterized

from bandits.Simulator import Simulator
from bandits.tests import TestBase


class HeuriticTest(TestBase):
    DECISION_EACH_SEC = 30

    @parameterized.expand(TestBase.TEST_SUITE)
    def test_heuristic(self, name, infrastructure):
        self.case_heuristic(name, infrastructure)

    def case_heuristic(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: Simulator):
            if simulator.now() % HeuriticTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        results = self.simulate(nodes, containers, TestBase.random_init, do_tick,
                                inspect.currentframe().f_code.co_name, name, f"Heuristic Reschedule 1- {name}")

        return results