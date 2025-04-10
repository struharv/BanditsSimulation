import logging
from logging import Logger

from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode


class Simulator(BaseSimulator):

    def __init__(self, nodes: list[ElectricNode], containers: list[Container], simulation_time=24*BaseSimulator.HOUR_SECONDS):
        super().__init__(nodes, containers, simulation_time)
        print("Simulator")

        if self.action_tick:
            self.action_init()

    def tick(self):
        super().tick()

        if self.orchestrator:
            self.orchestrator.tick(self.now())

        reward = self.compute_reward()
        self.reward_history += [(self.time, reward)]
        self.correct_placement += [(self.time, self.compute_correct())]


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
        for self.time in range(self.simulation_time_sec):

            if self.time % 100 == 0:
                print("tick", self.time)


            self.tick()

    def results(self):
        return {"cumulative reward": self.cumulative_reward()}

