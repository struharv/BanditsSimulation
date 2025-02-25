import sys

from engine.Container import Container


class Node:

    simulator = None

    PARAM_PERFORMANCE = 0.00
    PARAM_ENERGY = 0.9
    PARAM_COLOCATION = 0.0

    colocation = 0.0

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
        self.containers: list[Container] = []

        self.cpu_history: list[float] = []
        self.memory_mb_history: list[int] = []
        self.storage_mb_history: list[int] = []
        self.performance_history: list[int] = []

    def set_simulator(self, simulator):
        self.simulator = simulator

    def deploy(self, container: Container):
        self.containers += [container]

    def undeploy_all(self):
        self.containers = []

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
        self.performance_history += [self.compute_performance(self.containers)]

    def compute_reward(self) -> float:
        return self.compute_posible_reward(self.containers)

    def compute_posible_reward(self, containers, time_at=None):
        reward = 0
        #print(self.name)
        if time_at==None:
            time_at = self.simulator.time

        reward += self.compute_reward_at(time_at, containers)
        #    print(reward)

        return reward

    def compute_performance(self, containers=[]):
        performance = 1.0

        for container in containers:
            performance *= (1.0-container.performance_slowdown)

        return performance

    def compute_colocation(self, containers):
        return self.colocation ** (len(containers)+1)

    def compute_reward_at(self, time, containers):
        reward = 0
        for container in containers:
            reward += self.PARAM_ENERGY * container.cpu * self.green_at(time) + self.PARAM_PERFORMANCE * self.compute_performance(containers) + self.PARAM_COLOCATION* self.compute_colocation(containers)

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

    def get_context(self):
        pass
