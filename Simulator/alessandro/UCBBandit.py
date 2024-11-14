import math
from random import random

import numpy as np

from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator

def simple_max(Q, N, t):
    return np.random.choice(np.flatnonzero(Q == Q.max())) # breaking ties randomly

class UCBBandit(Orchestrator):
    CONTEXT_DIM = 3

    def __init__(self):
        self.b = None
        self.A = None
        print("UCBBandit.__init__")
        self.alpha = 0.1

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
        for node in self.simulator.nodes:
            energy = node.green_at(self.simulator.now())
            if result_node == None or energy < minEnergy:
                result_node = node
                minEnergy = energy

        return result_node





    def tick(self, time_s: int):
        if time_s % 30 != 0:
            return

        Pt = self.calculateUCB()

        maxIndex, maxP = self.select_arm(Pt)

        # take action
        worst_node = self.worstNodeWithContainer()
        if worst_node and len(worst_node.containers) > 0:
            self.simulator.migrate(worst_node.containers[0].name, self.simulator.nodes[maxIndex].name)

        #update reward


        print("UCBBANDIT tick!", time_s, maxIndex, maxP)

    def select_arm(self, Pt):
        maxP = None
        maxIndex = None
        for i in range(len(Pt)):
            if maxP == None or Pt[i] > maxP:
                maxP = Pt[i]
                maxIndex = i
        return maxIndex, maxP

    def calculateUCB(self):
        O = []
        Pt = []
        for node_i in range(len(self.simulator.nodes)):
            node = self.simulator.nodes[node_i]

            context = np.array(node.get_context(self.simulator.now()))

            A_inv = np.linalg.inv(self.A[node_i])
            theta = np.dot(A_inv, self.b[node_i])

            x = context.reshape([-1, 1])

            p = np.dot(theta.T, x) + self.alpha * np.sqrt(np.dot(x.T, np.dot(A_inv, x)))

            O += [theta]
            Pt += [p]
        return Pt


