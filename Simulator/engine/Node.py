import sys


class Node:

    simulator = None

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int, green_points: list[tuple[int, float]]):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
        self.green_points = green_points
        self.containers = []

    def set_simulator(self, simulator):
        self.simulator = simulator

    def deploy(self, container):
        self.containers += [container]

    def reset_containers(self):
        """
        Undeploy all containers
        :return:
        """
        self.containers = []

    def tick(self):
        pass

    def compute_reward(self) -> float:
        reward = 0

        for container in self.containers:
            reward += container.cpu_req * self.green_at(self.simulator.time)

        return reward

    def add_green_points(self, green_points):
        self.green_points = green_points

    def green_at(self, at_time):
        if len(self.green_points) < 2:
            return 0

        pointStart = 0
        pointStartY = 0

        pointEnd = sys.maxsize
        pointEndY = sys.maxsize

        for point in self.green_points:

            x = point[0]
            y = point[1]

            if x == at_time:
                return y

            if x < at_time:
                #if x >= pointStart:
                pointStart = x
                pointStartY = y

            if x > at_time and pointEnd == sys.maxsize:
                #if x < pointEnd:
                pointEnd = x
                pointEndY = y

        if pointEnd == sys.maxsize:
            return pointStartY

        result = pointStartY + float(pointEndY-pointStartY) / (pointEnd-pointStart) * (at_time-pointStart)
        #result = pointStartY + float(pointEndY-pointStartY)*at_time / float(pointEnd-pointStart)
        print(f"start = {pointStart}, {pointStartY}; end = {pointEnd}, {pointEndY} result = {result}")

        return result