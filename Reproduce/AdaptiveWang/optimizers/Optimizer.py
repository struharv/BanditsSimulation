import math

from Processor import Processor
from User import User


class Optimizer:
    def __init__(self, users: list[User], servers: list[Processor], arms):
        self.users = users
        self.servers = servers
        self.arms = arms



    def tick(self) -> float:
        pass

    def reward(self, arm):
        if len(self.users) != len(arm):
            print("ERROR: len(self.users) != len(arm)")
            return -1

        result_reward = 0
        for user in range(len(arm)):
            where_execute = arm[user]
            if where_execute == -1:
                result_reward = max(result_reward, self.users[user].process_locally())
            else:
                result_reward = max(result_reward, self.users[user].proces_remotely( self.servers[where_execute]))

        return result_reward

