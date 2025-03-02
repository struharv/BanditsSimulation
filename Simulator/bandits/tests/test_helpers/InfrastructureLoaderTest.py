import unittest

from bandits.tests.test_helpers.InfrastructureLoader import InfrastructureLoader


class InfrastructureLoaderTest(unittest.TestCase):
    def test_load(self):
        nodes, containers = InfrastructureLoader.load("infrastructures/infrastructure1_test_simple.json")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(len(containers), 2)


if __name__ == '__main__':
    unittest.main()
