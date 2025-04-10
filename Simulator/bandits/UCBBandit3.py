import numpy
import numpy as np

import random
from bandits.Orchestrator import Orchestrator
from engine.Container import Container
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

class ClassOrchestrator:
    def __init__(self, K_arms: int, d: int, alpha=0.5):
        self.K_arms = K_arms
        self.linucb_arms = [LinucbArm(arm_index=i, d=d, alpha=alpha) for i in range(K_arms)]

    def select_arm(self, x_array):
        highest_ucb = -1

        candidate_arms = []
        all_arms = []
        # all_arms = []

        for arm_index in range(self.K_arms):
            arm_ucb = self.linucb_arms[arm_index].calc_UCB(x_array)
            all_arms += [(arm_index, arm_ucb)]
            # print(arm_index, arm_ucb)

            if arm_ucb > highest_ucb:
                highest_ucb = arm_ucb
                candidate_arms = [arm_index]

            if arm_ucb == highest_ucb:
                candidate_arms.append(arm_index)

        chosen_arm = np.random.choice(candidate_arms)
        all_arms.sort(key=lambda x: x[1], reverse=True)

        print(all_arms)
        return all_arms


class UCBBandit3(Orchestrator):

    def __init__(self, K_arms: int, d: int, alpha=0.5):

        self.class_linucbs : list[ClassOrchestrator] = None
        self.K_arms = K_arms
        self.d = d
        self.alpha = alpha
        self.randomness = 0.05
        #self.linucb_arms = [LinucbArm(arm_index=i, d=d, alpha=alpha) for i in range(K_arms)]



    def init(self):
        super().init()
        self.class_linucbs = []
        for i in range(self.simulator.get_highest_perfclass()+1):
            self.class_linucbs += [ClassOrchestrator(self.K_arms, self.d, self.alpha)]
        
        self.class_linucb = ClassOrchestrator(self.K_arms, self.d, self.alpha)


    def tick(self, time_s: int):
        if time_s % 30 != 0:
            return

        print("------", time_s, "------")
        print("context", self.make_array_context(time_s))

        # observe context
        x = np.array(self.make_array_context(time_s))

        # find good node based on the context
        # selected_arm = random.randint(0, len(self.simulator.nodes)-1)

        worst_node = self.worst_node_with_container()
        if random.random() < self.randomness:
            worst_node = self.random_node_with_container()
            
        print("worst node", worst_node)
        worst_container = None
        if worst_node and len(worst_node.containers) > 0:
            worst_container = random.choice(worst_node.containers)

        if not worst_container:
            return

        all_arms = self.class_linucbs[worst_container.perfclass].select_arm(x)

        #all_arms = self.class_linucb.select_arm(x)# self.select_arm(x)

        for i in range(min(20, len(all_arms))):
            selected_arm = all_arms[i][0]

            if random.random() < self.randomness:
                selected_arm = random.randint(0, self.K_arms-1)

            # decide which container to migrate & migrate
            if worst_node and len(worst_node.containers) > 0:
                if not self.simulator.migrate(worst_container.name, self.simulator.nodes[selected_arm].name):
                    print("no migration")
                    continue

                # get reward
                reward = self.simulator.compute_reward() + 0.01*numpy.random.normal(loc=0.0, scale=1, size=None)
                print(f"{selected_arm}: reward {reward}")

                # update arm
                self.class_linucbs[worst_container.perfclass].linucb_arms[selected_arm].reward_update(reward, x)
                break
                #self.class_linucb.linucb_arms[selected_arm].reward_update(reward, x)

    def make_array_context(self, time_s: int):
        res = []

        for node in self.simulator.nodes:
            context = node.get_context(time_s)
            for context_item in context:
                res += [context_item]
                #res += [0]

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


    def random_node_with_container(self) -> Node:
        result_node = None
        minEnergy = None
        shuffled = []

        for node in self.simulator.nodes:
            if len(node.containers) > 0:
                shuffled += [node]

        random.shuffle(shuffled)

        return shuffled[0]


