import logging
from logging import Logger

from engine.Container import Container
from engine.Node import Node
from engine.bandits.Orchestrator import Orchestrator


class BaseSimulator:
    TIME_MAX_MINUTES = 24*60*60
    EVENT_MIGRATE = "migration"

    def __init__(self, nodes: list[Node], containers: list[Container]):
        self.nodes = nodes
        self.containers = containers
        self.orchestrator = None
        self.time = 0

        self.action_tick = None
        self.action_init = None

        self.orchestration_events: list[tuple[2]] = []

        self.reward_history: list[tuple[int, float]] = []

        for node in nodes:
            node.set_simulator(self)

    def set_orchestrator(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator
        orchestrator.set_simulator(self)

    def set_action_tick(self, action_tick):
        self.action_tick = action_tick

    def set_action_init(self, action_init):
        self.action_init = action_init

    def tick(self):
        logging.debug("BaseSimulator.do_tick")

        for node in self.nodes:
            node.tick()

        if self.action_tick:
            self.action_tick(self)

    def reset(self):
        for node in self.nodes:
            node.reset_containers()

    def simulate(self):
        pass

    def now(self) -> int:
        return self.time

    def orchestration_event(self, node_name: str, event: str):
        self.orchestration_events += [(self.now(), node_name, event)]

