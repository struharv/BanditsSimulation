from bandits.Simulator import Simulator


class HeuristicHelper:
    def sort_by_performance(simulator: Simulator):
        for container in simulator.containers:
            node = simulator.find_container_in_node(container.name)
