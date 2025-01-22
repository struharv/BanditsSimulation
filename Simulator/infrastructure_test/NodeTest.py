import unittest

from bandits.NewSimulator import NewSimulator
from engine.ElectricNode import ElectricNode




class NodeTest(unittest.TestCase):

    def test_node_green_at1(self):
        node = ElectricNode("abc", 0, 0, 0, [(0, 0), (5, 1), (10, 0)])
        node.green_at(5)

        self.assertEqual(1, node.green_at(5))

        self.assertEqual(0, node.green_at(0))
        self.assertEqual(0, node.green_at(10))
        self.assertEqual(0, node.green_at(20))

        self.assertEqual(0.5, node.green_at(2.5))

    def test_node_green_at2(self):
        node = ElectricNode("abcx", 0, 0, 0, [(0, 1), (5, 2), (10, 0)])
        self.assertEqual(1.5, node.green_at(2.5))

    def test_node_green_at3(self):
        node = ElectricNode("abcx", 0, 0, 0, [(0, 1), (5, 2), (10, 0.5)])
        self.assertEqual(0.5, node.green_at(15))

    def test_node_green_two_points(self):
        node = ElectricNode("abcx", 0, 0, 0, [(0, 0.5), (NewSimulator.TIME_MAX_SECONDS, 0.5)])
        self.assertEqual(0.5, node.green_at(15))

    def test_node_green_advanced(self):
        node = ElectricNode("node1", 1, 1024, 500, [(7 * NewSimulator.HOUR_SECONDS, 0.0), (12 * NewSimulator.HOUR_SECONDS, 0.5), (14 * NewSimulator.HOUR_SECONDS, 0.5), (19 * NewSimulator.HOUR_SECONDS, 0.0)])

        self.assertEqual(0, node.green_at(19 * 60 + 1))





if __name__ == '__main__':
    unittest.main()
