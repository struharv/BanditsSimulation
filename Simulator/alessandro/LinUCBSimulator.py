import logging
from logging import Logger

from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node


class LinUCBSimulator(BaseSimulator):

    def __init__(self, nodes: list[ElectricNode], containers: list[Container]):
        super().__init__(nodes, containers)


    def tick(self):
        super().tick()

        logging.debug("LinUCBSimulator.tick")
        if self.now() % 10:
            self.orchestration_event(self.nodes[0].name, "XXX")

    def update_nodes(self):
        for node in self.nodes:
            node.tick()


    def simulate(self):
        # init

        for self.time in range(self.TIME_MAX_MINUTES):
            self.update_nodes()
            self.tick()

