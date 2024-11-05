class Container:
    cpu_req = 0
    memory_req = 0
    storage_req = 0
    name = ""

    def __init__(self, name: str, cpu_req: float, memory_req: int, storage_req: int):
        self.name = name
        self.cpu_req = cpu_req
        self.memory_req = memory_req
        self.storage_req = storage_req
