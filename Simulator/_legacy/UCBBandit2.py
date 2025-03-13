import math
import random

import numpy as np

from engine.Node import Node
from engine.bandits.Orchestrator import Orchestrator
from numpy.linalg import inv


def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max()))  # breaking ties randomly


class UCBBandit2(Orchestrator):

    def __init__(self, narms, ndims, alpha):
        # Set number of arms
        self.narms = narms
        # Number of context features
        self.ndims = ndims
        # explore-exploit parameter
        self.alpha = alpha
        # Instantiate A as a ndims×ndims matrix for each arm
        self.A = np.zeros((self.narms, self.ndims, self.ndims))
        # Instantiate b as a 0 vector of length ndims.
        self.b = np.zeros((narms, self.ndims, 1))
        # set each A per arm as identity matrix of size ndims
        for arm in range(self.narms):
            self.A[arm] = np.eye(self.ndims)

    def play(self, tround, context):
        # gains per each arm
        p_t = np.zeros(self.ndims)

        # ===============================
        #    MAIN LOOP ...
        # ===============================
        for i in range(self.ndims):
            # initialize theta hat
            self.theta = inv(self.A[i]).dot(self.b[i])
            # get context of each arm from flattened vector of length 100
            cntx = context[i * 10:(i + 1) * 10]
            # get gain reward of each arm
            p_t[i] = self.theta.T.dot(cntx
                                      ) + self.alpha * np.sqrt(
                cntx.dot(inv(self.A[i]).dot(cntx)))
        action = np.random.choice(np.where(p_t == max(p_t))[0])
        # np.argmax returns values 0-9, we want to compare with arm indices in dataset which are 1-10
        # Hence, add 1 to action before returning
        return action + 1

    def update(self, arm, reward, context):
        self.A[arm] = self.A[arm] + np.outer(context[arm * 10:(arm + 1) * 10], context[arm * 10:(arm + 1) * 10])
        self.b[arm] = np.add(self.b[arm].T, context[arm * 10:(arm + 1) * 10] * reward).reshape(self.ndims, 1)
        return


    def init(self):
        print("init")

        print("building An")
        self.A = []
        self.b = []

        self.CONTEXT_DIM = len(self.simulator.nodes)

        for node in self.simulator.nodes:
            self.A += [np.identity(self.CONTEXT_DIM)]
            self.b += [np.zeros([self.CONTEXT_DIM, 1])]

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
            self.simulator.migrate(random.choice(worst_node.containers).name,
                                   self.simulator.nodes[best_expected_reward_arm_index].name)

        # update reward
        reward = self.simulator.compute_reward()
        x = contexts[best_expected_reward_arm_index]
        x = x.reshape([-1, 1])
        self.A[best_expected_reward_arm_index] += + np.dot(x, x.T)
        self.b[best_expected_reward_arm_index] += reward * x

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


