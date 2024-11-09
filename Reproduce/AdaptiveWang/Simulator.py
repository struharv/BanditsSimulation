from optimizers.Optimizer import Optimizer


class Simulator:
    MAX_STEPS = 100

    def __init__(self, optimizer: Optimizer):
        self.optimizer = optimizer
        self.time = 0

    def simulate(self):

        for self.time in range(self.MAX_STEPS):
            print(f"simulator: tick: {self.time}")
            self.optimizer.tick()