import inspect
import unittest

from bandits.Simulator import Simulator
from bandits.Orchestrator import Orchestrator
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Node import Node

from visual.Visualizer import Visualizer


class VisualizerTest(unittest.TestCase):
    NODES = [ElectricNode("node1", 1, 1024, 500, [(7 * Simulator.HOUR_SECONDS, 0.0), (12 * Simulator.HOUR_SECONDS, 0.5), (14 * Simulator.HOUR_SECONDS, 0.5), (19 * Simulator.HOUR_SECONDS, 0.0)]),
             ElectricNode("node2", 1, 1024, 500, [(0, 0.2), (24 * Simulator.HOUR_SECONDS, 0.2)]),
             ElectricNode("node3", 1, 1024, 500, [(5 * Simulator.HOUR_SECONDS, 0.0), (10 * Simulator.HOUR_SECONDS, 0.5), (12 * Simulator.HOUR_SECONDS, 0.5), (17 * Simulator.HOUR_SECONDS, 0.0)])
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
