from engine.BaseSimulator import BaseSimulator
from engine.Container import Container
from engine.Node import Node
from engine.bandits.Bandit import Bandit


class Simulator(BaseSimulator):
    TIME_MAX_MINUTES = 60 * 24

    def __init__(self, nodes: list[Node], containers: list[Container]):
        super().__init__(nodes, containers)

    def orchestrate(self):
        if not self.orchestrator:
            return

        self.orchestrator.tick(self.time)

    def tick(self):

        self.orchestrate()

        reward = self.compute_reward()
        self.reward_history += [(self.time, reward)]

        print(f"tick {self.time}")

    def compute_reward(self) -> float:
        reward = 0
        for node in self.nodes:
            reward += node.compute_reward()

        return reward

    def max_reward(self):
        pass

    def simulate(self):

        for self.time in range(self.TIME_MAX_MINUTES):
            self.tick()

    def total_reward(self) -> float:
        result = 0
        for reward in self.reward_history:
            result += reward

        return result


