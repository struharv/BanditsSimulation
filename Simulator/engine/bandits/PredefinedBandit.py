import random

from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Bandit import Bandit


class PredefinedBandit(Bandit):
    def __init__(self, definition: list[tuple[int, int]]):
        self.definition = definition


    def tick(self, time_s: int):
        print("BANDIT tick!", self.simulator.TIME_MAX_MINUTES)

        self.simulator.reset()

        #for self.definition

        for container in self.simulator.containers:
            self.random_node().deploy(container)

    def random_node(self) -> Node:
        nodes_len = len(self.simulator.nodes)
        return self.simulator.nodes[random.randint(0, nodes_len-1)]



