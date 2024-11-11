from generators.TaskGenerator import TaskGenerator
from optimizers.Optimizer import Optimizer


class Simulator:
    MAX_STEPS = 100

    def __init__(self, optimizer: Optimizer, generator: TaskGenerator):
        self.optimizer = optimizer
        self.generator = generator
        self.time = 0
        self.rewards = []

    def simulate(self):
        self.rewards = []
        for self.time in range(self.MAX_STEPS):

            if self.generator:
                self.generator.generate()

            reward = self.optimizer.tick()
            print(f"simulator: tick: {self.time} {reward}")
            self.rewards += [reward]



