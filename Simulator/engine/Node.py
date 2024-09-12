import sys


class Node:
    cpu = 1.0
    memory_mb = 1024
    storage_mb = 5000

    containers = []
    simulator = None

    green_points = []

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int, green_points: list[tuple[int, float]]):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
        self.green_points = green_points

    def set_simulator(self, simulator):
        self.simulator = simulator

    def deploy(self, container):
        self.containers += [container]

    def reset_containers(self):
        self.containers = []

    def tick(self):
        pass

    def compute_reward(self) -> int:
        reward = 0
        for container in self.containers:
            pass

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
                if x >= pointStart:
                    pointStart = x
                    pointStartY = y

            if x > at_time:
                if x < pointEnd:
                    pointEnd = x
                    pointEndY = y

        if pointEnd == sys.maxsize:
            return pointStartY

        result = pointStartY + (float(pointEndY-pointStartY) / (pointEnd-pointStart)) * at_time
        print(f"{pointStart}, {pointEnd}, {result}")

        return result