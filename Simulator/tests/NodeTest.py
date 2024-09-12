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


    def test_node_green_advanced(self):
        node = Node("node1", 1, 1024, 500, [(7 * 60, 0.0), (12 * 60, 0.5), (14 * 60, 0.5), (19 * 60, 0.0)])

        #self.assertEqual(0, node.green_at(0))
        #self.assertEqual(0, node.green_at(7*60-1))
        self.assertEqual(0, node.green_at(19 * 60 + 1))



if __name__ == '__main__':
    unittest.main()
