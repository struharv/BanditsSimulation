import inspect
import unittest
import random

from parameterized import parameterized

from alessandro.NewSimulator import NewSimulator
from alessandro.UCBBandit import UCBBandit
from alessandro.tests.JustTest import JustTest
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from engine.bandits.MultiArmBandit import MultiArmBandit
from visual.Visualizer import Visualizer


class UCBBanditTest(JustTest):

    @parameterized.expand(JustTest.TEST_SUITE)
    def test_UCB_bandit(self, name, infrastructure):

        nodes, containers = infrastructure

        bandit = UCBBandit()
        self.do_simulation(nodes, containers, JustTest.random_init, None, inspect.currentframe().f_code.co_name + "_" + name,f"UCB - {name}",
                           orchestrator=bandit)

    @parameterized.expand(JustTest.TEST_SUITE)
    def test_UCB_bandit_alpha0_1(self, name, infrastructure):
        nodes, containers = infrastructure

        bandit = UCBBandit(alpha=0.1)
        self.do_simulation(nodes, containers, JustTest.random_init, None,
                           inspect.currentframe().f_code.co_name + "_" + name, f"UCB - {name}",
                           orchestrator=bandit)