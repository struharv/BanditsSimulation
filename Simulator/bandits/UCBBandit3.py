import numpy as np

import random
from bandits.Orchestrator import Orchestrator
from engine.Node import Node


class LinucbArm:

    def __init__(self, arm_index, d, alpha):
        self.theta = None
        self.arm_index = arm_index
        self.alpha = alpha

        self.A = np.identity(d)
        self.b = np.zeros([d, 1])

    def calc_UCB(self, x_array):
        A_inv = np.linalg.inv(self.A)

        self.theta = np.dot(A_inv, self.b)
        
        x = x_array.reshape([-1, 1])

        p = np.dot(self.theta.T, x) + self.alpha * np.sqrt(np.dot(x.T, np.dot(A_inv, x)))

        return p

    def reward_update(self, reward, x_array):
        x = x_array.reshape([-1, 1])

        self.A += np.dot(x, x.T)
        self.b += reward * x


class UCBBandit3(Orchestrator):

    def __init__(self, K_arms: int, d: int, alpha=0.5):
        self.K_arms = K_arms
        self.linucb_arms = [LinucbArm(arm_index=i, d=d, alpha=alpha) for i in range(K_arms)]

    def tick(self, time_s: int):
        if time_s % 30 != 0:
            return

        print("------", time_s, "------")
        print("context", self.make_array(time_s))

        # observe context
        x = np.array(self.make_array(time_s))

        # find good node based on the context
        # selected_arm = random.randint(0, len(self.simulator.nodes)-1)
        selected_arm = self.select_arm(x)

        # decide which container to migrate & migrate
        worst_node = self.worst_node_with_container()
        print("worst node", worst_node)
        if worst_node and len(worst_node.containers) > 0:
            self.simulator.migrate(random.choice(worst_node.containers).name,
                                   self.simulator.nodes[selected_arm].name)

            # get reward
            reward = self.simulator.compute_reward()
            print(f"{selected_arm}: reward {reward}")

            # update arm
            self.linucb_arms[selected_arm].reward_update(reward, x)

    def make_array(self, time_s: int):
        res = []
        for node in self.simulator.nodes:
            res += [node.get_context(time_s)]

        return res

    def worst_node_with_container(self) -> Node:
        result_node = None
        minEnergy = None
        shuffled = []

        for node in self.simulator.nodes:
            if len(node.containers) > 0:
                shuffled += [node]

        random.shuffle(shuffled)

        for node in shuffled:
            energy = node.green_at(self.simulator.now())
            if result_node == None or energy < minEnergy:
                result_node = node
                minEnergy = energy

        return result_node

    def select_arm(self, x_array):
        highest_ucb = -1

        candidate_arms = []

        for arm_index in range(self.K_arms):
            arm_ucb = self.linucb_arms[arm_index].calc_UCB(x_array)
            print(arm_index, arm_ucb)

            if arm_ucb > highest_ucb:
                highest_ucb = arm_ucb
                candidate_arms = [arm_index]

            if arm_ucb == highest_ucb:
                candidate_arms.append(arm_index)

        chosen_arm = np.random.choice(candidate_arms)

        return chosen_arm
