class User:
    def __init__(self, name: str, processor):
        self.name = name
        self.processor = processor

        self.task_size  = None
        self.deadline = None


    def generate(self, size=100, deadline = 100):
        self.task_size = size
        self.deadline = deadline

    def process_locally(self):
        return self.processor.process(self.task_size)

    def proces_remotely(self, processor):
        max_size_local = self.deadline * self.processor.computation_capacity / self.processor.d

        if max_size_local >= self.task_size:
            return self.process_locally()
        else:

            remote = self.task_size - max_size_local

            return self.deadline + processor.process(remote)




class Processor:
    def __init__(self, name: str, computation_capacity: float):
        self.name = name
        self.computation_capacity = computation_capacity
        self.d = 1

    def process(self, task_size):
        return task_size / self.computation_capacity


class Bandit:
    pass


class Simulator:
    def __init__(self, users : list[User] = None, servers : list[Processor] = [None]):
        self.users = users
        self.servers = servers

    def simulate(self):

        for t in range(100):

            for user in self.users:
                user.generate()

    def reward(self, action: list[int]):
        result = 0

        for ac in range(len(action)):

            k = action[ac]
            if k == -1: # process locally
                latency = self.users[ac].process_locally()
            else:
                latency = self.users[ac].proces_remotely(self.servers[k])

            result = max(result, latency)



        return result









