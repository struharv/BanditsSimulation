import unittest

from engine.Container import Container
from engine.Node import Node
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer


class VisualizerTest(unittest.TestCase):
    def test_visualize(self):
        nodes = [Node("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5)]),
                 Node("node2", 1, 1024, 500, [(0, 0.5), (Simulator.TIME_MAX, 0.5)]),
                 Node("node3", 1, 1024, 500, [])]

        containers = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulator = Simulator(nodes, containers)

        visualizer = Visualizer(simulator)
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
