from bandits.NewSimulator import NewSimulator
from engine.Container import Container
from engine.ElectricNode import ElectricNode


def spikes(amount, height, shift=0):
    res = []
    for i in range(amount):
        peak = (NewSimulator.TIME_MAX_SECONDS / amount) * i
        res += [(peak - 1 * NewSimulator.HOUR_SECONDS - shift, 0.0)]
        res += [(peak, height)]
        res += [(peak + 1 * NewSimulator.HOUR_SECONDS - shift, 0.0)]
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
                              [(0 * NewSimulator.HOUR_SECONDS, 0.8),
                               (24 * NewSimulator.HOUR_SECONDS, 0.8)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.1, 25, 10),
                      Container("container3", 0.1, 25, 10),
                      Container("container4", 0.1, 25, 10),
                      Container("container5", 0.1, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_still_containers(container_cnt: int, cpu: float, memory: int, storage: int):
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.2),
                               (24 * NewSimulator.HOUR_SECONDS, 0.2)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.8),
                               (24 * NewSimulator.HOUR_SECONDS, 0.8)])]

        containers = []
        for i in range(container_cnt):
            containers += [Container(f"container{i}", cpu, memory, storage)]

        return nodes, containers

    @staticmethod
    def make_infrastructure_increasing_containers(container_cnt: int, cpu: float, memory: int, storage: int):
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.2),
                               (24 * NewSimulator.HOUR_SECONDS, 0.2)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.9)])]

        containers = []
        for i in range(container_cnt):
            containers += [Container(f"containers{containers}", cpu, memory, storage)]

        return nodes, containers

    @staticmethod
    def make_infrastructure_superstill():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)])]

        containers = [Container("container1", 0.2, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.2, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_extreme_still():
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node2", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.1)]),

                 ElectricNode("node3", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.8),
                               (24 * NewSimulator.HOUR_SECONDS, 0.8)])]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_spikey(container_cnt: int, cpu: float, memory: int, storage: int):
        nodes = [ElectricNode("node1", 1, 1024, 500,

                              spikes(3, 0.8)),

                 ElectricNode("node2", 1, 1024, 500,
                              spikes(10, 0.2)),

                 ElectricNode("node3", 1, 1024, 500,
                              spikes(5, 0.5))]

        containers = []
        for i in range(container_cnt):
            containers += [Container(f"containers{containers}", cpu, memory, storage)]

        return nodes, containers

    @staticmethod
    def make_infrastructure_spikey5(count=5):
        nodes = []
        for cnt in range(5):
            nodes += [ElectricNode(f"node{cnt + 1}", 1, 1024, 500,
                                   spikes(10, (1.0 / count) * (cnt + 1)))]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers

    @staticmethod
    def make_infrastructure_real_1():
        nodes = [
            # czech
            ElectricNode("node1", 1, 1024, 500,

                         [(0 * NewSimulator.HOUR_SECONDS, 0.1041),
                          (1 * NewSimulator.HOUR_SECONDS, 0.0966),
                          (2 * NewSimulator.HOUR_SECONDS, 0.0973),
                          (3 * NewSimulator.HOUR_SECONDS, 0.11359999999999999),
                          (4 * NewSimulator.HOUR_SECONDS, 0.1295),
                          (5 * NewSimulator.HOUR_SECONDS, 0.17800000000000002),
                          (6 * NewSimulator.HOUR_SECONDS, 0.2206),
                          (7 * NewSimulator.HOUR_SECONDS, 0.2285),
                          (8 * NewSimulator.HOUR_SECONDS, 0.21539999999999998),
                          (9 * NewSimulator.HOUR_SECONDS, 0.21059999999999998),
                          (10 * NewSimulator.HOUR_SECONDS, 0.2059),
                          (11 * NewSimulator.HOUR_SECONDS, 0.2059),
                          (12 * NewSimulator.HOUR_SECONDS, 0.1949),
                          (13 * NewSimulator.HOUR_SECONDS, 0.1845),
                          (14 * NewSimulator.HOUR_SECONDS, 0.1889),
                          (15 * NewSimulator.HOUR_SECONDS, 0.2034),
                          (16 * NewSimulator.HOUR_SECONDS, 0.22460000000000002),
                          (17 * NewSimulator.HOUR_SECONDS, 0.2163),
                          (18 * NewSimulator.HOUR_SECONDS, 0.2323),
                          (19 * NewSimulator.HOUR_SECONDS, 0.20350000000000001),
                          (20 * NewSimulator.HOUR_SECONDS, 0.1883),
                          (21 * NewSimulator.HOUR_SECONDS, 0.16870000000000002),
                          (22 * NewSimulator.HOUR_SECONDS, 0.15259999999999999),
                          (23 * NewSimulator.HOUR_SECONDS, 0.1465)
                          ]),
            # sweden
            ElectricNode("node2", 1, 1024, 500,
                         [(0 * NewSimulator.HOUR_SECONDS, 0.1697),
                          (1 * NewSimulator.HOUR_SECONDS, 0.15810000000000002),
                          (2 * NewSimulator.HOUR_SECONDS, 0.158),
                          (3 * NewSimulator.HOUR_SECONDS, 0.1535),
                          (4 * NewSimulator.HOUR_SECONDS, 0.19390000000000002),
                          (5 * NewSimulator.HOUR_SECONDS, 0.26940000000000003),
                          (6 * NewSimulator.HOUR_SECONDS, 0.3299),
                          (7 * NewSimulator.HOUR_SECONDS, 0.33759999999999996),
                          (8 * NewSimulator.HOUR_SECONDS, 0.3689),
                          (9 * NewSimulator.HOUR_SECONDS, 0.3979),
                          (10 * NewSimulator.HOUR_SECONDS, 0.3948),
                          (11 * NewSimulator.HOUR_SECONDS, 0.386),
                          (12 * NewSimulator.HOUR_SECONDS, 0.3996),
                          (13 * NewSimulator.HOUR_SECONDS, 0.3957),
                          (14 * NewSimulator.HOUR_SECONDS, 0.3486),
                          (15 * NewSimulator.HOUR_SECONDS, 0.2847),
                          (16 * NewSimulator.HOUR_SECONDS, 0.2484),
                          (17 * NewSimulator.HOUR_SECONDS, 0.22329999999999997),
                          (18 * NewSimulator.HOUR_SECONDS, 0.22390000000000002),
                          (19 * NewSimulator.HOUR_SECONDS, 0.21739999999999998),
                          (20 * NewSimulator.HOUR_SECONDS, 0.21660000000000001),
                          (21 * NewSimulator.HOUR_SECONDS, 0.1474),
                          (22 * NewSimulator.HOUR_SECONDS, 0.0931),
                          (23 * NewSimulator.HOUR_SECONDS, 0.0874)]),

            ElectricNode("node3", 1, 1024, 500,
                         [(0 * NewSimulator.HOUR_SECONDS, 0.4268),
                          (1 * NewSimulator.HOUR_SECONDS, 0.4035),
                          (2 * NewSimulator.HOUR_SECONDS, 0.39759999999999995),
                          (3 * NewSimulator.HOUR_SECONDS, 0.3862),
                          (4 * NewSimulator.HOUR_SECONDS, 0.3883),
                          (5 * NewSimulator.HOUR_SECONDS, 0.39649999999999996),
                          (6 * NewSimulator.HOUR_SECONDS, 0.4275),
                          (7 * NewSimulator.HOUR_SECONDS, 0.5268999999999999),
                          (8 * NewSimulator.HOUR_SECONDS, 0.6268),
                          (9 * NewSimulator.HOUR_SECONDS, 0.6627),
                          (10 * NewSimulator.HOUR_SECONDS, 0.6862),
                          (11 * NewSimulator.HOUR_SECONDS, 0.6970999999999999),
                          (12 * NewSimulator.HOUR_SECONDS, 0.7045999999999999),
                          (13 * NewSimulator.HOUR_SECONDS, 0.7112999999999999),
                          (14 * NewSimulator.HOUR_SECONDS, 0.7008),
                          (15 * NewSimulator.HOUR_SECONDS, 0.6920999999999999),
                          (16 * NewSimulator.HOUR_SECONDS, 0.6797),
                          (17 * NewSimulator.HOUR_SECONDS, 0.6252),
                          (18 * NewSimulator.HOUR_SECONDS, 0.5443),
                          (19 * NewSimulator.HOUR_SECONDS, 0.5161),
                          (20 * NewSimulator.HOUR_SECONDS, 0.5209),
                          (21 * NewSimulator.HOUR_SECONDS, 0.5162),
                          (22 * NewSimulator.HOUR_SECONDS, 0.5175),
                          (23 * NewSimulator.HOUR_SECONDS, 0.5192)])]

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

                              spikes(5, 1)),

                 ElectricNode("node2", 1, 1024, 500,
                              spikes(8, 0.8)),

                 ElectricNode("node3", 1, 1024, 500,
                              spikes(10, 0.2)),

                 ElectricNode("node4", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.8),
                               (24 * NewSimulator.HOUR_SECONDS, 0.2)]),

                 ElectricNode("node5", 1, 1024, 500,
                              [(0 * NewSimulator.HOUR_SECONDS, 0.1),
                               (24 * NewSimulator.HOUR_SECONDS, 0.9)])
                 ]

        containers = [Container("container1", 0.1, 25, 10),
                      Container("container2", 0.2, 25, 10),
                      Container("container3", 0.15, 25, 10),
                      Container("container4", 0.11, 25, 10),
                      Container("container5", 0.07, 25, 10),
                      ]

        return nodes, containers
