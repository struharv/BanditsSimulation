from engine.Container import Container
from engine.Node import Node
from engine.bandits.Bandit import Bandit


class BaseSimulator:
    def __init__(self, nodes: list[Node], containers: list[Container]):
        self.nodes = nodes
        self.containers = containers
        self.orchestrator = None
        self.time = 0

        self.reward_history: list[tuple[int, float]] = []
        for node in nodes:
            node.set_simulator(self)

    def set_orchestrator(self, orchestrator: Bandit):
        self.orchestrator = orchestrator
        orchestrator.set_simulator(self)

    def tick(self):
        pass

    def reset(self):
        for node in self.nodes:
            node.reset_containers()

    def simulate(self):
        pass
