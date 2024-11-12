import sys

from engine.Container import Container


class Node:

    simulator = None

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
        self.containers: list[Container] = []


        self.cpu_history: list[float] = []
        self.memory_mb_history: list[int] = []
        self.storage_mb_history: list[int] = []


    def set_simulator(self, simulator):
        self.simulator = simulator

    def deploy(self, container: Container):
        self.containers += [container]

    def reset_containers(self):
        """
        Undeploy all containers
        :return:
        """
        self.containers = []

    def tick(self):
        self.cpu_history += [0]
        self.memory_mb_history += [0]
        self.storage_mb_history += [0]


    def compute_reward(self) -> float:
        reward = 0

        for container in self.containers:
            reward += container.cpu * self.green_at(self.simulator.time)

        return reward


    def now_cpu_used(self):
        res = 0
        for container in self.containers:
               res += container.cpu
