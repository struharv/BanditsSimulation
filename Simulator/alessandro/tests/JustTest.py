import random
import unittest


from alessandro.NewSimulator import NewSimulator
from alessandro.tests.test_helpers.Infrastructure import Infrastructure
from alessandro.tests.test_helpers.Stats import Stats
from visual.Visualizer import Visualizer


class JustTest(unittest.TestCase):
    STATS_REPETITIONS = 10

    TEST_SUITE = [
        ["still", Infrastructure.make_infrastructure_still()],
        ["spikey", Infrastructure.make_infrastructure_spikey()],
        ["bigspikey", Infrastructure.make_infrastructure_bigspikey()],
        ["spikey5", Infrastructure.make_infrastructure_spikey5()],
    ]

    def simulate(self, nodes, containers, do_init, do_tick, test_file_name: str, title: str, orchestrator=None, visualize=True):
        simulator = NewSimulator(nodes, containers)
        simulator.set_orchestrator(orchestrator)
        simulator.set_action_tick(do_tick)
        simulator.set_action_init(do_init)

        simulator.simulate()

        if visualize:
            visualizer = Visualizer(simulator, test_file_name)
            visualizer.draw(title)

        return simulator.results()

    def perform_stats(self, test_name, case_function, test_suite):
        stat = Stats()
        for instance in range(JustTest.STATS_REPETITIONS):

            for param in test_suite:
                print(instance, test_name, param[0])
                result = case_function(param[0], param[1])
                stat.add_result(test_name, param[0], instance, result)

        stat.export_raw(f"plots/stats_{test_name}.csv")
        stat.export_summary(f"plots/stats_{test_name}_summary.csv")


    @staticmethod
    def random_init(simulator: NewSimulator):
        buf_containers = []
        for cont in simulator.containers:
            buf_containers += [cont]

        while len(buf_containers) > 0:
            if simulator.migrate(buf_containers[0].name, random.choice(simulator.nodes).name):
                del buf_containers[0]