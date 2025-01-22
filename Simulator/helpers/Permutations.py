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
        self.do_permuatate([], 0)

        self.make_sets()

    def assignment_to_set(self, assignment):
        res_set = []
        for _ in self.nodes:
            res_set += [[]]

        for cont_i in range(len(assignment)):
            node = assignment[cont_i]
            res_set[node] += [self.containers[cont_i]]


        return res_set





    def make_sets(self):
        result_sets = []
        for assignment in self.results:
            res = self.assignment_to_set(assignment)
            print(assignment, res)
            for sets in res:
                if

        return result_sets



    def do_permuatate(self, assignments, position):
        if position >= len(self.containers):
            print("done", assignments)
            self.results += [assignments]
            return

        for node in range(len(self.nodes)):

            new_assignments = copy.deepcopy(assignments)
            new_assignments += [node]
            self.do_permuatate(new_assignments, position+1)





if __name__ == '__main__':
    nodes, containers = Infrastructure.make_infrastructure_still()

    perm = Permutations(nodes, containers)
    perm.make_permutations()
