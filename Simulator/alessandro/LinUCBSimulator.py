from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node


class LinUCBSimulator(BaseSimulator):

    def __init__(self, nodes: list[ElectricNode], containers: list[Container]):
        super().__init__(nodes, containers)


    def tick(self):
        print("LinUCBSimulator.tick")


    def update_nodes(self):
        for node in self.nodes:
            node.tick()


    def simulate(self):
        # init

        for self.time in range(self.TIME_MAX_MINUTES):
            self.update_nodes()
            self.tick()

        # observe context
        pass