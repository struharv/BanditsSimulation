import logging
import sys

from engine.Container import Container
from engine.Node import Node

import numpy

class ElectricNode(Node):
    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int, green_points: list[tuple[int, float]], perfclass=None):
        super().__init__(name, cpu, memory_mb, storage_mb, perfclass=perfclass)

        self.green_points = green_points
        self.containers: list[Container] = []

        # last x ticks
        self.green_energy_history: list[float] = []

    def add_green_points(self, green_points):
        self.green_points = green_points

    def tick(self):
        super().tick()
        logging.debug(f"Node {self.name} tick")
        if self.simulator:
            self.green_energy_history += [self.green_at(self.simulator.now())]
        else:
            logging.debug(f"WARNING: No simulator assigned to node {self.name}")

    def green_at(self, at_time) -> float:

        # we need at least 2 points
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
        logging.debug(f"start = {pointStart}, {pointStartY}; end = {pointEnd}, {pointEndY} result = {result}")

        return result
 
    def get_context(self, time_s: int):
        #return [self.green_at(time_s), 1.0-self.current_cpu_usage()]
        return [self.green_at(time_s), 1.0 - self.current_cpu_usage()]

    def __repr__(self):
        return f"Node.{self.name}{self.cpu, self.memory_mb, self.storage_mb}"

