import logging
import random
from logging import Logger

from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator


class RandomBandit(Orchestrator):
    def __init__(self):
        pass

    def tick(self, time_s: int):
        logging.debug("BANDIT tick!", self.simulator.TIME_MAX_MINUTES)

        self.simulator.reset()
        for container in self.simulator.containers:
            self.random_node().deploy(container)

    def random_node(self) -> Node:
        nodes_len = len(self.simulator.nodes)
        return self.simulator.nodes[random.randint(0, nodes_len-1)]



