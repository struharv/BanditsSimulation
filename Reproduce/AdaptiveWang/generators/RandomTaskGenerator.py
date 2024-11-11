import random
from random import Random

from User import User
from generators.TaskGenerator import TaskGenerator


class RandomTaskGenerator(TaskGenerator):
    def __init__(self, users: list[User], deadline: int, intStart: int, intStop: int ):
        super(RandomTaskGenerator, self).__init__(users)
        self.deadline = deadline
        self.intStart = intStart
        self.intStop = intStop


    def generate(self):
        for user in self.users:
            user.generate(random.randint(self.intStart, self.intStop), self.deadline)