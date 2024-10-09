class Orchestrator:
    def __init__(self):
        self.simulator = None

    def set_simulator(self, simulator):
        self.simulator = simulator

    def tick(self, time_s: int):
        pass

class Bandit(Orchestrator):
    pass



