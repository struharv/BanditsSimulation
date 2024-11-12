class Container:
    cpu = 0
    memory_mb = 0
    storage_mb = 0
    name = ""

    def __init__(self, name: str, cpu_req: float, memory_req: int, storage_req: int):
        self.name = name
        self.cpu = cpu_req
        self.memory_mb = memory_req
        self.storage_mb = storage_req
