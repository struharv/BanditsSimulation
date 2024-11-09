from random import random

import numpy as np


from Processor import Processor
from Simulator import Simulator
from User import User
from optimizers.Optimizer import Optimizer


def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max()))  # breaking ties randomly


class Bandit(Optimizer):
    def __init__(self, arms):
        self.arms = arms

        self.epsilon = 0.2
        self.alpha = 0.1

        self.k = len(self.arms)
        self.Q = np.ones(self.k)  # initial Q
        self.N = np.zeros(self.k)  # initalize number of rewards given

        self.rewards = np.zeros(Simulator.MAX_STEPS)
        self.actions = np.zeros(Simulator.MAX_STEPS)

    def tick(self, time_s: int):
        #print("BANDIT tick!", self.simulator.TIME_MAX_MINUTES)

        arm = 0
        if np.random.rand() < self.epsilon: # explore
            arm = random.randint(0, len(self.arms) - 1)
        else:  # exploit
            arm = simple_max(self.Q, self.N, 0)

        self.N[arm] += 1
        #self.deploy_set(self.arms[arm])
        #reward = self.simulator.compute_reward()

        if self.alpha > 0:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) * self.alpha
        else:
            self.Q[arm] = self.Q[arm] + (reward - self.Q[arm]) / self.N[arm]
