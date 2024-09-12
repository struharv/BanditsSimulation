from engine.Container import Container
from engine.Node import Node
from engine.bandits.Bandit import Bandit


class Simulator:
    TIME_MAX = 60*24


    def __init__(self, nodes: list[Node], containers: list[Container]):
        self.nodes = nodes
        self.containers = containers
        self.bandit = None
        self.time = 0

        self.reward_history: list[tuple[int, float]] = []
        for node in nodes:
            node.set_simulator(self)

    def add_bandit(self, bandit: Bandit):
        self.bandit = bandit
        bandit.set_simulator(self)

    def orchestrate(self):
        if not self.bandit:
            return

        self.bandit.tick(self.time)

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

    def reset(self):
        for node in self.nodes:
            node.reset_containers()

    def simulate(self):

        for self.time in range(self.TIME_MAX):
            self.tick()

    def total_reward(self) -> float:
        result = 0
        for reward in self.reward_history:
            result += reward

        return result

