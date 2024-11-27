import inspect
import logging
import random
import unittest
from logging import Logger


from alessandro.NewSimulator import NewSimulator
from alessandro.tests.Infrastructure import Infrastructure
from alessandro.tests.JustTest import JustTest
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer
from parameterized import parameterized






class HeuristicTest(JustTest):
    DECISION_EACH_SEC = 30

    @parameterized.expand(JustTest.TEST_SUITE)
    def test_random(self, name, infrastructure):
        nodes, containers = infrastructure

        def do_tick(simulator: Simulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                simulator.migrate(random.choice(containers).name,  random.choice(nodes).name)

        self.do_simulation(nodes, containers, JustTest.random_init, do_tick, inspect.currentframe().f_code.co_name+"_"+name, f"Random Reschedule - {name}")

    def test_random_lowest_reward_first(self):
        nodes, containers = Infrastructure.make_infrastructure()

        def do_tick(simulator: Simulator):
            if simulator.now() % HeuristicTest.DECISION_EACH_SEC == 0:
                for container in containers:
                    pass

                simulator.migrate(random.choice(containers).name, random.choice(nodes).name)

        self.do_simulation(nodes, containers, JustTest.random_init, do_tick, inspect.currentframe().f_code.co_name, "xxx")


if __name__ == '__main__':
    unittest.main()