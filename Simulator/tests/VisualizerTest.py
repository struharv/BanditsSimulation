import inspect
import unittest

from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node
from engine.Simulator import Simulator
from engine.bandits.Orchestrator import Orchestrator

from engine.bandits.PredefinedBandit import PredefinedBandit
from engine.bandits.RandomBandit import RandomBandit
from visual.Visualizer import Visualizer


class VisualizerTest(unittest.TestCase):
    NODES = [ElectricNode("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5), (19 * 60, 0.0)]),
             ElectricNode("node2", 1, 1024, 500, [(0, 0.2), (Simulator.TIME_MAX_MINUTES, 0.2)]),
             ElectricNode("node3", 1, 1024, 500, [(5 * 60, 0.0), (10 * 60, 0.5), (12 * 60, 0.5), (17 * 60, 0.0)])
             ]

    CONTAINERS = [Container("container1", 0.5, 256, 100),
                  Container("container2", 0.5, 256, 100)]

    def test_visualize(self):

        simulator = Simulator(self.NODES, self.CONTAINERS)
        #self.NODES[0].deploy(self.CONTAINERS[0])
        #self.NODES[2].deploy(self.CONTAINERS[1])

        simulator.set_orchestrator(Orchestrator())
        simulator.simulate()

        visualizer = Visualizer(simulator, inspect.currentframe().f_code.co_name)
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
