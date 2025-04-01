import random

import numpy as np

from bandits.Simulator import Simulator
from engine.Node import Node
from bandits.Orchestrator import Orchestrator


def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max())) # breaking ties randomly

class MultiArmBandit(Orchestrator):
    def __init__(self, sets):
        self.sets = sets

        self.epsilon = 0.1
        self.alpha = 0.5

        self.k = len(self.sets)
        self.Q = np.ones(self.k) # initial Q
        self.N = np.zeros(self.k)  # initalize number of rewards given

        #self.rewards = np.zeros(Si  mulator.DEFAULT_SIMULATION_TIME)
        #self.actions = np.zeros(Simulator.DEFAULT_SIMULATION_TIME)

    def tick(self, time_s: int, decisioneach_s = 30):
        if time_s % decisioneach_s != 0:
            return

        if np.random.rand() < self.epsilon:
            # explore
            arm = random.randint(0, len(self.sets)-1)
        else:
            # exploit
            arm = simple_max(self.Q, self.N, 0)

        self.N[arm] += 1

        self.deploy_set(self.sets[arm])
        reward = self.simulator.compute_reward()

        if self.alpha > 0:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) * self.alpha
        else:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) / self.N[arm]

    def deploy_set(self, deploy_set):
        self.simulator.reset()

        for deploy in deploy_set:
            node = deploy[0]

            for container in deploy[1]:
                node.deploy(container)

    def random_node(self) -> Node:
        nodes_len = len(self.simulator.nodes)
        return self.simulator.nodes[random.randint(0, nodes_len-1)]

