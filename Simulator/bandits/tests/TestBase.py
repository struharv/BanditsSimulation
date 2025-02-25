import os
import random
import unittest


from bandits.NewSimulator import NewSimulator
from bandits.tests.test_helpers.Infrastructure import Infrastructure
from bandits.tests.test_helpers.Stats import Stats
from helpers.Permutations import Permutations
from visual.Visualizer import Visualizer


class TestBase(unittest.TestCase):
    STATS_REPETITIONS = 5
    ENABLE_STATS = False
    OUT_DIR = "plots/"

    TEST_SUITE = [
        #["superstill", Infrastructure.make_infrastructure_superstill()],
        ["still", Infrastructure.make_infrastructure_still()],
        ["still_3_container", Infrastructure.make_infrastructure_still_containers(3, 0.2, 10, 10)],
        ["still_4_container", Infrastructure.make_infrastructure_still_containers(4, 0.2, 10, 10)],
        ["still_5_container", Infrastructure.make_infrastructure_still_containers(5, 0.2, 10, 10)],

        #["extreme_still", Infrastructure.make_infrastructure_extreme_still()],

        #["spikey", Infrastructure.make_infrastructure_spikey()],
        #["bigspikey", Infrastructure.make_infrastructure_bigspikey()],
        #["spikey5", Infrastructure.make_infrastructure_spikey5()],
    ]

    def simulate(self, nodes, containers, do_init, do_tick, directory, test_file_name: str, title: str, orchestrator=None, visualize=True):
        simulator = NewSimulator(nodes, containers)
        simulator.set_orchestrator(orchestrator)
        simulator.set_action_tick(do_tick)
        simulator.set_action_init(do_init)

        simulator.simulate()

        if visualize:
            test_out_dir = f"{self.OUT_DIR}{directory}"
            if not os.path.isdir(test_out_dir):
                os.mkdir(test_out_dir)

            visualizer = Visualizer(simulator, f"{test_out_dir}/{test_file_name}")
            visualizer.draw(title)

        return simulator.results()

    def perform_stats(self, test_name, case_function, test_suite, explicit_repetitions = None):
        if not self.ENABLE_STATS:
            return

        print(f"Perform Stats: {test_name}")

        stat = Stats()

        repetitions = TestBase.STATS_REPETITIONS
        if explicit_repetitions:
            repetitions = explicit_repetitions

        for instance in range(repetitions):

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

    def make_possible_deployments(self, nodes, containers):
        permutations = Permutations(nodes, containers)
        sets = permutations.make_permutations()

        return sets
