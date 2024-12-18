from alessandro.NewSimulator import NewSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode


def spikes(amount, height):
    res = []
    for i in range(amount):
        peak = (NewSimulator.TIME_MAX_SECONDS / amount) * i
        res += [(peak - 1 * NewSimulator.HOUR_SECONDS, 0.0)]
        res += [(peak, height)]
        res += [(peak + 1 * NewSimulator.HOUR_SECONDS, 0.0)]
    return res


class Infrastructure:

    @staticmethod
    def make_infrastructure():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0.4 * NewSimulator.HOUR_SECONDS, 0.0),
                               (1.0 * NewSimulator.HOUR_SECONDS, 0.9),
                               (1.6 * NewSimulator.HOUR_SECONDS, 0.9),
                               (3 * NewSimulator.HOUR_SECONDS, 0.0),
                               (7 * NewSimulator.HOUR_SECONDS, 0.0),

                               (12 * NewSimulator.HOUR_SECONDS, 0.5),
                               (14 * NewSimulator.HOUR_SECONDS, 0.5)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(7 * NewSimulator.HOUR_SECONDS, 0.0),
                               (12 * NewSimulator.HOUR_SECONDS, 0.4),
                               (15 * NewSimulator.HOUR_SECONDS, 0.8),
                               (17 * NewSimulator.HOUR_SECONDS, 0.0),
                               (20 * NewSimulator.HOUR_SECONDS, 0.4)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (12 * NewSimulator.HOUR_SECONDS, 0.4),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_still():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.2),
                               (24 * NewSimulator.HOUR_SECONDS, 0.2)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.3),
                               (24 * NewSimulator.HOUR_SECONDS, 0.3)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_spikey():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              spikes(3, 0.8)),

                 ElectricNode("node2", 1, 1024, 500,
                              spikes(10, 0.2)),

                 ElectricNode("node3", 1, 1024, 500,
                              spikes(5, 0.5))]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_spikey5(count = 5):
        nodes = []
        for cnt in range(5):
            nodes += [ElectricNode(f"node{cnt+1}", 1, 1024, 500,
                              spikes(10, (1.0/count) * (cnt+1)))]


        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_bigspikey():

        nodes = [ElectricNode("node1", 1, 1024, 500,

                              spikes(10, 1)),

                 ElectricNode("node2", 1, 1024, 500,
                              spikes(10, 1)),

                 ElectricNode("node3", 1, 1024, 500,
                              spikes(10, 1))]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers




