import logging
import random

import numpy as np

from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator


def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max())) # breaking ties randomly

class MultiArmBandit(Orchestrator):
    def __init__(self, sets):
        self.sets = sets

        self.epsilon = 0.2
        self.alpha  = 0.1

        self.k = len(self.sets)
        self.Q = np.ones(self.k) # initial Q
        self.N = np.zeros(self.k)  # initalize number of rewards given

        self.rewards = np.zeros(Simulator.TIME_MAX_MINUTES)
        self.actions = np.zeros(Simulator.TIME_MAX_MINUTES)


    def tick(self, time_s: int):
        logging.debug("BANDIT tick!", self.simulator.TIME_MAX_MINUTES)

        self.simulator.reset()

        # explore
        arm = 0
        if np.random.rand() < self.epsilon:
            arm = random.randint(0, len(self.sets)-1)
        else: # exploit
            arm = simple_max(self.Q, self.N, 0)

        self.N[arm] += 1
        self.deploy_set(self.sets[arm])
        reward = self.simulator.compute_reward()

        if self.alpha > 0:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) * self.alpha
        else:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) / self.N[arm]




    def deploy_set(self, deploy_set):
        for deploy in deploy_set:
            node = deploy[0]

            for container in deploy[1]:
                node.deploy(container)




    def random_node(self) -> Node:
        nodes_len = len(self.simulator.nodes)
        return self.simulator.nodes[random.randint(0, nodes_len-1)]



