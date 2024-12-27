import inspect
import unittest
import random

from parameterized import parameterized

from alessandro.NewSimulator import NewSimulator
from alessandro.tests.JustTest import JustTest
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.bandits.MultiArmBandit import MultiArmBandit
from visual.Visualizer import Visualizer


class NaiveBanditTest(JustTest):


    @parameterized.expand(JustTest.TEST_SUITE)
    def test_naive_bandit(self, name, infrastructure):
        self.case_naive_bandit(name, infrastructure)

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

            [(nodes[1], [containers[0]]), (nodes[2], [containers[1], containers[2], containers[3], containers[4]])],
            [(nodes[2], [containers[0]]), (nodes[1], [containers[1], containers[2], containers[3], containers[4]])],


            [(nodes[0], [containers[0]]), (nodes[1], [containers[1]]), (nodes[2], [containers[2], containers[3], containers[4]])],
            [(nodes[0], [containers[1]]), (nodes[1], [containers[0]]), (nodes[2], [containers[2], containers[3], containers[4]])],

        ]

        bandit = MultiArmBandit(sets)
        result = self.do_simulation(nodes, containers, None, None, inspect.currentframe().f_code.co_name + "_" + name,
                           f"Naive Bandit - {name}", orchestrator=bandit)
        return result

    def test_naive_bandit(self):
        self.do_test_stats("test_naive_bandit", self.case_naive_bandit, JustTest.TEST_SUITE)