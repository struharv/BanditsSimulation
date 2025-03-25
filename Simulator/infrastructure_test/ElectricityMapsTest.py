import inspect
import unittest

from bandits.NewSimulator import NewSimulator
from bandits.Orchestrator import Orchestrator
from electricitymaps.ElectricityMaps import ElectricityMaps
from electricitymaps.ElectricityMaps2 import ElectricityMap2Node
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from visual.Visualizer import Visualizer


class ElectricityMapsTest(unittest.TestCase):

    def test_visualize_timezones(self):
        elMap = ElectricityMaps()
        elMap.read_all_countries()
        elMap.align_database("AT", 2024, 20, 21)

        NODES = [ElectricNode("node1", 1, 1024, 500, ElectricityMap2Node.toGreen("ES", 2024, 8, 20)),
                 ElectricNode("node2", 1, 1024, 500, ElectricityMap2Node.toGreen("NZ", 2024, 8, 20))]

        CONTAINERS = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]


        simulator = NewSimulator(NODES, CONTAINERS)
        # self.NODES[0].deploy(self.CONTAINERS[0])
        # self.NODES[2].deploy(self.CONTAINERS[1])

        simulator.set_orchestrator(Orchestrator())
        simulator.simulate()

        visualizer = Visualizer(simulator, inspect.currentframe().f_code.co_name)
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
