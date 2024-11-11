from Processor import Processor
from User import User
from optimizers.Optimizer import Optimizer


class RandomOptimizer(Optimizer):
    def __init__(self, users: list[User], servers: list[Processor],  arms):
        super(RandomOptimizer, self).__init__(users, servers, arms)

    def tick(self) -> float:
        print("RandomOptimizer: tick")

        arm = self.arms[0]

        res_reward = self.reward(arm)

        return res_reward
