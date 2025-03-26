import inspect
import unittest

from bandits.NewSimulator import NewSimulator
from bandits.RandomBandit import RandomBandit
from engine.Container import Container
from engine.ElectricNode import ElectricNode

from visual.Visualizer import Visualizer


class RandomBanditTest(unittest.TestCase):

    def create(self):
        self.NODES = [ElectricNode("node1", 1, 1024, 500, [(7 * NewSimulator.HOUR_SECONDS, 0.0), (12 * NewSimulator.HOUR_SECONDS, 0.5), (14 * NewSimulator.HOUR_SECONDS, 0.5), (19 * NewSimulator.HOUR_SECONDS, 0.0)]),
                      ElectricNode("node2", 1, 1024, 500, [(0, 0.2), (NewSimulator.time_max_seconds, 0.2)]),
                      ElectricNode("node3", 1, 1024, 500, [(5 * NewSimulator.HOUR_SECONDS, 0.0), (10 * NewSimulator.HOUR_SECONDS, 0.5), (12 * NewSimulator.HOUR_SECONDS, 0.5), (17 * NewSimulator.HOUR_SECONDS, 0.0)])
                      ]

        self.CONTAINERS = [Container("container1", 0.5, 256, 100),
                           Container("container2", 0.5, 256, 100),
                           Container("container3", 0.5, 256, 100),
                           Container("container4", 0.5, 256, 100),
                           Container("container5", 0.5, 256, 100), ]

    def test_visualize_random(self):
        self.create()

        simulator = NewSimulator(self.NODES, self.CONTAINERS)
        #self.NODES[0].deploy(self.CONTAINERS[0])
        #self.NODES[2].deploy(self.CONTAINERS[1])

        simulator.set_orchestrator(RandomBandit())
        simulator.simulate()

        visualizer = Visualizer(simulator, inspect.currentframe().f_code.co_name)
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
