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

    def undeploy(self, container_name) -> bool:
        for index_container in range(len(self.containers)):
            if container_name == self.containers[index_container].name:
                del self.containers[index_container]

                return True

        return False


    def reset_containers(self):
        """
        Undeploy all containers
        :return:
        """
        self.containers = []

    def tick(self):
        self.cpu_history += [self.now_cpu_used()]
        self.memory_mb_history += [self.now_memory_mb_used()]
        self.storage_mb_history += [self.now_storage_mb_used()]


    def compute_reward(self) -> float:
        reward = 0

        for container in self.containers:
            reward += container.cpu * self.green_at(self.simulator.time)

        return reward

    def now_cpu_used(self):
        res = 0
        for container in self.containers:
            res += container.cpu

        return res

    def now_memory_mb_used(self):
        res = 0
        for container in self.containers:
            res += container.memory_mb

        return res

    def now_storage_mb_used(self):
        res = 0
        for container in self.containers:
            res += container.storage_mb

        return res

    def can_accommodate(self, container: Container) -> bool:
        if self.now_cpu_used() + container.cpu > self.cpu:
            return False

        if self.now_memory_mb_used() + container.memory_mb > self.memory_mb:
            return False

        if self.now_storage_mb_used() + container.storage_mb > self.storage_mb:
            return False

        return True
