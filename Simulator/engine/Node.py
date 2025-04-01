import sys

from engine.Container import Container


class Node:

    # simulator that controls this node
    simulator = None

    # parameters to compute the reward value
    PARAM_PERFORMANCE = 0
    PARAM_PERFORMANCE_PERFMATRIX = 0
    PARAM_ENERGY = 1.0
    PARAM_COLOCATION = 0.0

    colocation = 0.5

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int, perfclass=None):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
        self.perfclass = perfclass

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


    def reset_containers(self) -> None:
        """
        Undeploy all containers
        :return:
        """
        self.containers = []

    def tick(self):
        self.cpu_history += [self.current_cpu_usage()]
        self.memory_mb_history += [self.current_memory_mb_usage()]
        self.storage_mb_history += [self.current_storage_mb_usage()]
        self.performance_history += [self.compute_performance(self.containers)]

    def compute_reward(self) -> float:
        return self.compute_posible_reward(self.containers)

    def compute_posible_reward(self, containers, time_at=None):
        reward = 0

        if not time_at:
            time_at = self.simulator.time

        reward += self.compute_reward_at(time_at, containers)

        return reward

    def compute_performance(self, containers=[]):
        performance = 1.0

        for container in containers:
            performance *= (1.0 - container.performance_slowdown)

        return performance

    def compute_colocation(self, containers):
        return self.colocation ** (len(containers)+1)

    def get_perf(self, container: Container):
        perfmatrix = self.simulator.perfmatrix

        if not perfmatrix or container.perfclass is None or self.perfclass is None:
            return 1.0

        return self.simulator.perfmatrix[self.perfclass][container.perfclass]

    def compute_reward_at(self, time, containers):
        reward = 0

        for container in containers:
            # energy: the higher green energy, the higher reward
            reward += self.PARAM_ENERGY * container.cpu * self.green_at(time) #

            # performance:
            reward += self.PARAM_PERFORMANCE * self.compute_performance(containers)

            # performance: perfmatrix
            reward += self.PARAM_PERFORMANCE_PERFMATRIX * self.get_perf(container)

            # colocation: more containers deployed, the less reward
            reward += self.PARAM_COLOCATION * self.compute_colocation(containers)

        return reward

    def current_cpu_usage(self):
        """
        Compute current cpu usage by deployed containers
        :return:
        """
        res = 0

        for container in self.containers:
            res += container.cpu

        return res

    def current_memory_mb_usage(self):
        res = 0
        for container in self.containers:
            res += container.memory_mb

        return res

    def current_storage_mb_usage(self):
        res = 0
        for container in self.containers:
            res += container.storage_mb

        return res

    def can_accommodate(self, container: Container) -> bool:
        if self.current_cpu_usage() + container.cpu > self.cpu:
            return False

        if self.current_memory_mb_usage() + container.memory_mb > self.memory_mb:
            return False

        if self.current_storage_mb_usage() + container.storage_mb > self.storage_mb:
            return False

        return True

    def get_context(self):
        return []
