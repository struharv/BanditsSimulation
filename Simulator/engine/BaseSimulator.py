from engine.Container import Container
from engine.Node import Node
from engine.bandits.Orchestrator import Orchestrator


class BaseSimulator:
    TIME_MAX_MINUTES = 60 * 24

    def __init__(self, nodes: list[Node], containers: list[Container]):
        self.nodes = nodes
        self.containers = containers
        self.orchestrator = None
        self.time = 0

        self.reward_history: list[tuple[int, float]] = []
        for node in nodes:
            node.set_simulator(self)

    def set_orchestrator(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator
        orchestrator.set_simulator(self)

    def tick(self):
        for node in self.nodes:
            node.tick()

    def reset(self):
        for node in self.nodes:
            node.reset_containers()

    def simulate(self):
        pass

    def now(self) -> int:
        return self.time
