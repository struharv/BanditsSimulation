import random
import unittest


from alessandro.NewSimulator import NewSimulator
from alessandro.tests.Infrastructure import Infrastructure
from engine.Simulator import Simulator
from visual.Visualizer import Visualizer
from parameterized import parameterized


class JustTest(unittest.TestCase):
    TEST_SUITE = [
        ["basic", Infrastructure.make_infrastructure()],
        ["still", Infrastructure.make_infrastructure_still()],
        ["spikey", Infrastructure.make_infrastructure_spikey()],
    ]

    DECISION_EACH_SEC = 30
    def do_simulation(self, nodes, containers, do_init, do_tick, test_name: str, orchestrator=None):
        simulatorUCB = NewSimulator(nodes, containers)
        simulatorUCB.set_orchestrator(orchestrator)
        simulatorUCB.set_action_tick(do_tick)
        simulatorUCB.set_action_init(do_init)

        simulatorUCB.simulate()

        visualizer = Visualizer(simulatorUCB, test_name)
        visualizer.draw()

    @staticmethod
    def random_init(simulator: Simulator):
        buf_containers = []
        for cont in simulator.containers:
            buf_containers += [cont]

        while len(buf_containers) > 0:
            if simulator.migrate(buf_containers[0].name, random.choice(simulator.nodes).name):
                del buf_containers[0]