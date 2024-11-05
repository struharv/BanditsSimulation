import unittest

from main import User, Processor


class BanditTest(unittest.TestCase):
    def test_processing(self):
        users = [User("user1", Processor("processor1", 10)),
                 User("user2", Processor("processor2", 10)),
                 User("user3", Processor("processor3", 10)),
                 ]

        servers = [Processor("server1", 100),
                   Processor("server2", 100),
                   Processor("server3", 100)]


        arms = [
            [-1, -1, -1],
            [0, -1, -1],
            [-1, 0, -1],
            [-1, -1, 0],
        ]

        users[0].generate(10)
        users[1].generate(10)
        users[2].generate(10)




