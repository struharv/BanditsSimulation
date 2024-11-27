import math
import random

import numpy as np

from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator

def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max())) # breaking ties randomly

class UCBBandit(Orchestrator):
    CONTEXT_DIM = 3

    def __init__(self, alpha=0.5):
        self.b = None
        self.A = None
        print("UCBBandit.__init__")
        self.alpha = 0.5

    def init(self):
        print("init")

        print("building An")
        self.A = []
        self.b = []
        
        for node in self.simulator.nodes:
            self.A += [np.identity(UCBBandit.CONTEXT_DIM)]
            self.b += [np.zeros([UCBBandit.CONTEXT_DIM, 1])]

        print(self.A)
        print(self.b)

    def worstNodeWithContainer(self) -> Node:
        result_node = None
        minEnergy = None
        shuffled = []
        for node in self.simulator.nodes:
            shuffled += [node]

        random.shuffle(shuffled)

        for node in shuffled:
            energy = node.green_at(self.simulator.now())
            if result_node == None or energy < minEnergy:
                result_node = node
                minEnergy = energy

        return result_node


    def tick(self, time_s: int):
        if time_s % 30 != 0:
            return

        p_values, theta_values, contexts = self.calculateUCB()

        best_expected_reward_arm_index = self.select_arm(p_values)

        # take action
        worst_node = self.worstNodeWithContainer()
        if worst_node and len(worst_node.containers) > 0:
            self.simulator.migrate(random.choice(worst_node.containers).name, self.simulator.nodes[best_expected_reward_arm_index].name)

        #update reward
        reward = self.simulator.compute_reward()
        x = contexts[best_expected_reward_arm_index]
        x = x.reshape([-1, 1])
        self.A[best_expected_reward_arm_index] += + np.dot(x, x.T)
        self.b[best_expected_reward_arm_index] += reward * x


        print("UCBBANDIT tick!", time_s, best_expected_reward_arm_index)

    def select_arm(self, Pt):
        maxP = -1
        maxIndex = []
        for i in range(len(Pt)):
            if Pt[i] > maxP:
                maxP = Pt[i]
                maxIndex = [i]
            else:
                if Pt[i] == maxP:
                    maxIndex += [i]

        return random.choice(maxIndex)

    def calculateUCB(self):
        theta_values = []
        p_values = []
        contexts = []
        for node_index in range(len(self.simulator.nodes)):
            node = self.simulator.nodes[node_index]
            context = np.array(node.get_context(self.simulator.now()))
            contexts += [np.copy(context)]

            A_inv = np.linalg.inv(self.A[node_index])
            theta = np.dot(A_inv, self.b[node_index])

            x = context.reshape([-1, 1])
            p = np.dot(theta.T, x) + self.alpha * np.sqrt(np.dot(x.T, np.dot(A_inv, x)))

            theta_values += [theta]
            p_values += [p]
        return p_values, theta_values, contexts


