class Container:
    cpu = 0
    memory_mb = 0
    storage_mb = 0
    name = ""
    performance_slowdown = 0.15

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb
