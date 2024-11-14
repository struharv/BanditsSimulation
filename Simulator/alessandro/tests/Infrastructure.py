from engine.Container import Container
from engine.ElectricNode import ElectricNode
from engine.Simulator import Simulator


class Infrastructure:

    @staticmethod
    def make_infrastructure():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0.8 * Simulator.HOUR_SECONDS, 0.0),
                               (1.0 * Simulator.HOUR_SECONDS, 0.9),
                               (1.2 * Simulator.HOUR_SECONDS, 0.0),
                               (7 * Simulator.HOUR_SECONDS, 0.0),

                               (12 * Simulator.HOUR_SECONDS, 0.5),
                               (14 * Simulator.HOUR_SECONDS, 0.5)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(7 * Simulator.HOUR_SECONDS, 0.0),
                               (12 * Simulator.HOUR_SECONDS, 0.4),
                               (15 * Simulator.HOUR_SECONDS, 0.8),
                               (17 * Simulator.HOUR_SECONDS, 0.0),
                               (20 * Simulator.HOUR_SECONDS, 0.4)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * Simulator.HOUR_SECONDS, 0.1),
                               (12 * Simulator.HOUR_SECONDS, 0.4),
                               (24 * Simulator.HOUR_SECONDS, 0.1)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers
