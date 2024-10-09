import unittest

from engine.Container import Container
from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.RandomBandit import RandomBandit
from visual.Visualizer import Visualizer


class BanditTest(unittest.TestCase):

    def create(self):
        self.NODES = [Node("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5), (19 * 60, 0.0)]),
                      Node("node2", 1, 1024, 500, [(0, 0.2), (Simulator.TIME_MAX_MINUTES, 0.2)]),
                      Node("node3", 1, 1024, 500, [(5 * 60, 0.0), (10 * 60, 0.5), (12 * 60, 0.5), (17 * 60, 0.0)])
                      ]

        self.CONTAINERS = [Container("container1", 0.5, 256, 100),
                           Container("container2", 0.5, 256, 100),
                           Container("container3", 0.5, 256, 100),
                           Container("container4", 0.5, 256, 100),
                           Container("container5", 0.5, 256, 100), ]

    def test_visualize(self):
        self.create()

        simulator = Simulator(self.NODES, self.CONTAINERS)
        #self.NODES[0].deploy(self.CONTAINERS[0])
        #self.NODES[2].deploy(self.CONTAINERS[1])

        simulator.set_orchestrator(RandomBandit())
        simulator.simulate()

        visualizer = Visualizer(simulator, prefix="RandomBandit_")
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
