import logging
import random

from engine.Container import Container
from engine.Exceptions.NoElementFoundException import NoElementFoundException
from engine.Node import Node
from bandits.Orchestrator import Orchestrator


class BaseSimulator:
    HOUR_SECONDS = 60*60
    TIME_MAX_SECONDS = 24 * HOUR_SECONDS

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

        if self.orchestrator:
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

    def init(self):
        pass

    def simulate(self):
        if self.action_init:
            self.action_init(self)

    def now(self) -> int:
        return self.time

    def orchestration_event(self, node_name: str, event: str):
        self.orchestration_events += [(self.now(), node_name, event)]

    def can_migrate(self, container, node):

        pass

    def deploy_as(self, deployment):
        for node_index in range(len(self.nodes)):
            node = self.nodes[node_index]
            node.undeploy_all()

            for container in deployment[node_index][1]:
                node.deploy(container)




    def migrate(self, container_name, node_name) -> bool:
        old_node = self.find_container_in_node(container_name)
        container = self.find_container(container_name)
        print(" migrating", container_name, "to", node_name)
        if not container:
            raise NoElementFoundException(f"Container {container_name} is not found.")

        new_node = self.find_node(node_name)
        if not new_node:
            raise NoElementFoundException(f"Node {node_name} is not found.")

        if not new_node.can_accommodate(container):
            return False

        if old_node:
            old_node.undeploy(container_name)

        new_node.deploy(container)

        return True


    def find_container_in_node(self, container_name: str) -> Node:
        for node in self.nodes:
            for container in node.containers:
                if container.name == container_name:
                    return node

        return None

    def find_node(self, node_name: str) -> Node:
        for node in self.nodes:
            if node_name == node.name:
                return node

        return None

    def find_container(self, container_name: str) -> Container:
        for container in self.containers:
            if container_name == container.name:
                return container

        return None

    def compute_reward(self) -> float:
        reward = 0
        for node in self.nodes:
            reward += node.compute_reward()

        return reward

    def compute_possible_reward(self, deployment, time) -> float:
        #print("computing possible reward")
        reward = 0
        for deployment_item in deployment:
            node = deployment_item[0]
            containers = deployment_item[1]

            reward += node.compute_posible_reward(containers, time)

            #for container in containers:
            #    #tmp = node.compute_reward_at(container.cpu, time)

            #    print(tmp)
            #    reward += tmp

        return reward

    def cumulative_reward(self) -> float:
        result = 0
        for reward in self.reward_history:
            result += reward[1]

        return result

    def random_init(self):
        """
        Randomly assign containers to nodes in the way the containers fullfil the constraints
        :param simulator:
        :return:
        """
        buf_containers = []
        for cont in self.containers:
            buf_containers += [cont]

        while len(buf_containers) > 0:
            if self.migrate(buf_containers[0].name, random.choice(self.nodes).name):
                del buf_containers[0]


