import inspect
import unittest
import random

from alessandro.LinUCBSimulator import LinUCBSimulator
from alessandro.tests.JustTest import JustTest
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator
from engine.bandits.MultiArmBandit import MultiArmBandit
from visual.Visualizer import Visualizer


class NaiveBanditTest(JustTest):

    def make_infrastructure(self):
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0.8 * Simulator.HOUR_SECONDS, 0.0),
                               (1.0 * Simulator.HOUR_SECONDS, 0.9),
                               (1.2 * Simulator.HOUR_SECONDS, 0.0),
                               (7 * Simulator.HOUR_SECONDS, 0.0),

                               (12 * Simulator.HOUR_SECONDS, 0.5),
                               (14 * Simulator.HOUR_SECONDS, 0.5)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(7 * Simulator.HOUR_SECONDS, 0.0),
                               (12 * Simulator.HOUR_SECONDS, 0.4),
                               (15 * Simulator.HOUR_SECONDS, 0.8),
                               (17 * Simulator.HOUR_SECONDS, 0.0),
                               (20 * Simulator.HOUR_SECONDS, 0.4)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * Simulator.HOUR_SECONDS, 0.1),
                               (12 * Simulator.HOUR_SECONDS, 0.4),
                               (24 * Simulator.HOUR_SECONDS, 0.1)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    def test_naive_bandit(self):
        nodes, containers = self.make_infrastructure()
        
        sets = [
            [(nodes[0], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],
            [(nodes[1], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],
            [(nodes[2], [containers[0], containers[1], containers[2], containers[3], containers[4]]), ],
            [(nodes[0], [containers[0], containers[1]]),  (nodes[1], [containers[1], containers[3], containers[4]])],
            [(nodes[1], [containers[0], containers[1]]),  (nodes[2], [containers[1], containers[3], containers[4]])],
            [(nodes[0], [containers[0], containers[1]]),  (nodes[2], [containers[1], containers[3], containers[4]])]
        ]

        bandit = MultiArmBandit(sets)
        self.do_simulation(nodes, containers, None, None, inspect.currentframe().f_code.co_name, orchestrator=bandit)