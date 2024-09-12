import unittest

from engine.Node import Node
from engine.Simulator import Simulator



class NodeTest(unittest.TestCase):
    def test_node_green_at1(self):
        node = Node("abc", 0, 0, 0, [(0, 0), (5, 1), (10, 0)])
        node.green_at(5)

        self.assertEqual(1, node.green_at(5))
        self.assertEqual(0, node.green_at(0))
        self.assertEqual(0, node.green_at(10))
        self.assertEqual(0, node.green_at(20))

        self.assertEqual(0.5, node.green_at(2.5))

    def test_node_green_at2(self):
        node = Node("abcx", 0, 0, 0, [(0, 1), (5, 2), (10, 0)])
        self.assertEqual(1.5, node.green_at(2.5))

    def test_node_green_at3(self):
        node = Node("abcx", 0, 0, 0, [(0, 1), (5, 2), (10, 0.5)])
        self.assertEqual(0.5, node.green_at(15))


    def test_node_green_two_points(self):
        node = Node("abcx", 0, 0, 0, [(0, 0.5), (Simulator.TIME_MAX, 0.5)])
        self.assertEqual(0.5, node.green_at(15))







if __name__ == '__main__':
    unittest.main()
