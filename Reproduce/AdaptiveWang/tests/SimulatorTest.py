import unittest

from Processor import Processor
from main import Simulator, User


class SimulatorTest(unittest.TestCase):
    def test_processing(self):
        user1 = User("user1", Processor("processor1", 10))
        user1.generate(10)
        self.assertEqual(1, user1.process_locally())

        user2 = User("user2", Processor("processor1", 10))
        user2.generate(100)
        self.assertEqual(10, user2.process_locally())

        user3 = User("user2", Processor("processor1", 10))
        user3.generate(100, deadline=1)
        self.assertEqual(1.9, user3.proces_remotely(Processor("", 100)))


    def test_action(self):

        users = [User("user1", Processor("processor1", 10)),
                 User("user2", Processor("processor2", 10)),
                 User("user3", Processor("processor3", 10)),
                 ]


        servers = [Processor("server1", 100),
                   Processor("server2", 100),
                   Processor("server3", 100)]

        users[0].generate(10)
        users[1].generate(10)
        users[2].generate(10)

        simulator = Simulator(users, servers)
        reward = simulator.reward([-1, -1, -1])
        self.assertEqual(1, reward)

        reward = simulator.reward([0, 0, 0])
        self.assertEqual(1, reward)

        users[0].generate(100, deadline=1)
        users[1].generate(100, deadline=1)
        users[2].generate(100, deadline=1)

        reward = simulator.reward([0, 0, 0])
        self.assertEqual(1.9, reward)



if __name__ == '__main__':
    unittest.main()
