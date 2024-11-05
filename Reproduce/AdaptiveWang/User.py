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
