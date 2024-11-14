import logging
from logging import Logger

from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node


class NewSimulator(BaseSimulator):

    def __init__(self, nodes: list[ElectricNode], containers: list[Container]):
        super().__init__(nodes, containers)

        if self.action_tick:
            self.action_init()


    def tick(self):
        super().tick()

        if self.orchestrator:
            self.orchestrator.tick(self.now())

        reward = self.compute_reward()
        self.reward_history += [(self.time, reward)]



    def simulate(self):
        # init
        super().init()
        super().simulate()

        for self.time in range(self.TIME_MAX_SECONDS):
            self.tick()

