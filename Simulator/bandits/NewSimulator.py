import logging
from logging import Logger

from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode


class NewSimulator(BaseSimulator):

    def __init__(self, nodes: list[ElectricNode], containers: list[Container]):
        super().__init__(nodes, containers)
        print("NewSimulator")
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
        print("Simulation start")
        super().init()

        if self.orchestrator:
            print("Orchestrator exists")
            self.orchestrator.init()

        print("super.simulate")
        super().simulate()
        print("/super.simulate")
        for self.time in range(self.TIME_MAX_SECONDS):
            '''
            if self.time % 10 == 0 or self.time > 86000:
                print("tick", self.time)
                for node in self.nodes:
                    print("\t", len(node.performance_history))
            '''

            self.tick()

    def results(self):
        return {"cumulative reward": self.cumulative_reward()}

