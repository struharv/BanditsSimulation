from bandits.NewSimulator import NewSimulator


class HeuristicHelper:
    def sort_by_performance(simulator: NewSimulator):
        for container in simulator.containers:
            node = simulator.find_container_in_node(container.name)
