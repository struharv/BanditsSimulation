class Processor:
    def __init__(self, name: str, computation_capacity: float):
        self.name = name
        self.computation_capacity = computation_capacity
        self.d = 1

    def process(self, task_size):
        return task_size / self.computation_capacity