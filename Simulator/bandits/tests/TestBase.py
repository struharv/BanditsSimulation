import os
import random
import unittest


from bandits.Simulator import Simulator
from bandits.tests.test_helpers.Infrastructure import Infrastructure
from bandits.tests.test_helpers.Stats import Stats
from helpers.Permutations import Permutations
from visual.Visualizer import Visualizer


class TestBase(unittest.TestCase):
    STATS_REPETITIONS = 15
    DECISION_PERIOD_SEC = 30
    ENABLE_STATS = False
    OUT_DIR = "plots/"
    """
    PERFMATRIX = [[1.0, 1.0, 1.0],
                  [0.8, 0.8, 0.8],
                  [0.8, 0.8, 0.8]]

    """
    PERFMATRIX = [[1.0, 0.7, 0.7],
                  [0.7, 1.0, 0.7],
                  [0.7, 0.7, 1.0]]

    """
    PERFMATRIX = [[1.1, 1.0, 1.0],
                  [1.0, 1.0, 1.0],
                  [1.0, 1.0, 1.0]]
    

    TEST_SUITE = [
        ["superstill_30_high", Infrastructure.make_infrastructure_superstill(container_cnt=30, container_cpu=0.8*3.0/30)],
        ["superstill_30_medium", Infrastructure.make_infrastructure_superstill(c
        ontainer_cnt=30, container_cpu=0.4 * 3.0/30)],
        ["superstill_30_low", Infrastructure.make_infrastructure_superstill(container_cnt=30, container_cpu=0.2 * 3.0/30)],
        #["still", Infrastructure.make_infrastructure_still()],

        #["Constant_Green_Energy", Infrastructure.make_infrastructure_still_containers(3, 0.2, 10, 10)],

        #["Real_30_high", Infrastructure.make_infrastructure_real_1(container_cnt=30, container_cpu=0.8*3.0/30)],
        #["Real_30_medium", Infrastructure.make_infrastructure_real_1(container_cnt=30, container_cpu=0.4 * 3.0 / 30)],
        #["Real_30_low", Infrastructure.make_infrastructure_real_1(container_cnt=30, container_cpu=0.2 * 3.0 / 30)],
    
        ["increasing_30_container_high", Infrastructure.make_infrastructure_3_nodes_increasing_containers(30, 0.8*3.0/30, 1, 1)],
        ["increasing_30_container_medium", Infrastructure.make_infrastructure_3_nodes_increasing_containers(30, 0.4 * 3.0 / 30, 1, 1)],
        ["increasing_30_container_low", Infrastructure.make_infrastructure_3_nodes_increasing_containers(30, 0.2*3.0/30, 1, 1)],

        ["bigspikey_30_container_high", Infrastructure.make_infrastructure_bigspikey_large_utilization(container_cnt=30, container_cpu=0.8*5.0/30)],
        ["bigspikey_30_container_medium", Infrastructure.make_infrastructure_bigspikey_large_utilization(container_cnt=30, container_cpu=0.4*5.0/30)],
        ["bigspikey_30_container_low",Infrastructure.make_infrastructure_bigspikey_large_utilization(container_cnt=30, container_cpu=0.2*5.0/30)],


        #["extreme_still", Infrastructure.make_infrastructure_extreme_still()],

        #["Varying_Green_Energy", Infrastructure.make_infrastructure_spikey(3, 0.2, 10, 10)],

        ####
 
        #["bigspikey", Infrastructure.make_infrastructure_bigspikey()],
        #["bigspikey_large_utilization", Infrastructure.make_infrastructure_bigspikey_large_utilization()],
        #["bigspikey_large_utilization_100containers", Infrastructure.make_infrastructure_bigspikey_large_utilization(container_cnt=100, container_cpu=0.01)],
        #["still_20_container", Infrastructure.make_infrastructure_still_containers(20, 0.01, 10, 10)],
        #["still_3_nodes_30_containers", Infrastructure.make_infrastructure_def_still(
        #                                3, 1, 10000, 10000,
        #                                30, 0.05, 1, 1)],
        #["still_30_nodes_1000_containers", Infrastructure.make_infrastructure_def_still(30, 1, 10, 10,
        #                                                                                20, 0.1, 10, 10)]
        #["spikey5", Infrastructure.make_infrastructure_spikey5()],
    ]

    def simulate(self, nodes, containers, do_init, do_tick, directory, test_file_name: str, title: str, orchestrator=None, visualize=True, perfmatrix=None, simulation_time=None):

        if simulation_time:
            simulator = Simulator(nodes, containers, simulation_time=simulation_time)
        else:
            simulator = Simulator(nodes, containers)

        simulator.set_perfmatrix(perfmatrix)
        simulator.set_orchestrator(orchestrator)
        simulator.set_action_tick(do_tick)
        simulator.set_action_init(do_init)

        print("about to simulate")
        simulator.simulate()
        print("simulation is done")

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
    def random_init(simulator: Simulator):
        """
        Randomly assign containers to nodes in the way the containers fullfil the constraints
        :param simulator:
        :return:
        """
        buf_containers = []
        for cont in simulator.containers:
            buf_containers += [cont]

        while len(buf_containers) > 0:
            #print(buf_containers[0].name)

            if simulator.migrate(buf_containers[0].name, random.choice(simulator.nodes).name):
                del buf_containers[0]
                #print(len(buf_containers))

    def compute_all_possible_deployments(self, nodes, containers):
        permutations = Permutations(nodes, containers)
        sets = permutations.make_permutations()

        return sets
