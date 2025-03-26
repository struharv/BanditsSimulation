import inspect
import unittest

from bandits.NewSimulator import NewSimulator
from bandits.Orchestrator import Orchestrator
from electricitymaps.ElectricityMaps2 import ElectricityMap2Node
from engine.Container import Container
from engine.ElectricNode import ElectricNode
from visual.Visualizer import Visualizer


class ElectricityMapsTest(unittest.TestCase):

    def test_visualize_timezones(self):
        days = 4
        NODES = [ElectricNode("nodeES", 1, 1024, 500, ElectricityMap2Node.toGreen("ES", 2024, 8, 20, limit=24*days+1)),
                 ElectricNode("nodePT", 1, 1024, 500, ElectricityMap2Node.toGreen("PT", 2024, 8, 20, limit=24*days+1)),
                 ElectricNode("nodeUS", 1, 1024, 500, ElectricityMap2Node.toGreen("US-NY-NYIS", 2024, 8, 20, limit=24*days+1)),
                 ElectricNode("nodeFR", 1, 1024, 500, ElectricityMap2Node.toGreen("FR", 2024, 8, 20, limit=24*days+1)),
                 ElectricNode("nodeHU", 1, 1024, 500, ElectricityMap2Node.toGreen("HU", 2024, 8, 20, limit=24*days+1))
                 ]

        CONTAINERS = [Container("container1", 0.5, 256, 100),
                      Container("container2", 0.5, 256, 100)]

        simulator = NewSimulator(NODES, CONTAINERS, simulation_time=24*days*NewSimulator.HOUR_SECONDS)

        simulator.set_orchestrator(Orchestrator())
        simulator.simulate()

        visualizer = Visualizer(simulator, inspect.currentframe().f_code.co_name)
        visualizer.draw()


if __name__ == '__main__':
    unittest.main()
