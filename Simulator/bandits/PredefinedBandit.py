import logging
import random
from logging import Logger

from engine.Node import Node
from engine.bandits.Orchestrator import Orchestrator


class PredefinedBandit(Orchestrator):
    def __init__(self, definition: list[tuple[int, int]]):
        self.definition = definition

    def tick(self, time_s: int):
        logging.debug("BANDIT tick!", self.simulator.simulation_time_sec)
        self.simulator.reset()

        for container in self.simulator.containers:
            self.random_node().deploy(container)

    def random_node(self) -> Node:
        nodes_len = len(self.simulator.nodes)
        return self.simulator.nodes[random.randint(0, nodes_len-1)]



