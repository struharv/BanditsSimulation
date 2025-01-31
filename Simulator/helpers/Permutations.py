import copy

from bandits.tests.test_helpers.Infrastructure import Infrastructure
from engine.Container import Container
from engine.Node import Node


class Permutations:
    def __init__(self, nodes:list[Node], containers:list[Container]):
        self.nodes = nodes
        self.containers = containers

        self.results = []

    def make_permutations(self):
        self.results = []
        self.do_permutate([], 0)

        return self.make_sets()

    def assignment_to_set(self, assignment):
        res_set = []
        for _ in self.nodes:
            res_set += [[]]

        for cont_i in range(len(assignment)):
            node = assignment[cont_i]
            res_set[node] += [self.containers[cont_i]]

        #
        nice_set = []
        for set_item in range(len(res_set)):
            nice_set += [(self.nodes[set_item], res_set[set_item])]

        return nice_set


    def make_sets(self):
        result_sets = []
        for assignment in self.results:
            res = self.assignment_to_set(assignment)
            result_sets += [res]
            print(assignment, res)

        return result_sets



    def do_permutate(self, assignments, position):
        if position >= len(self.containers):
            print("done", assignments)
            self.results += [assignments]
            return

        for node in range(len(self.nodes)):

            new_assignments = copy.deepcopy(assignments)
            new_assignments += [node]
            self.do_permutate(new_assignments, position + 1)





if __name__ == '__main__':
    nodes, containers = Infrastructure.make_infrastructure_still()

    perm = Permutations(nodes, containers)
    perm.make_permutations()
