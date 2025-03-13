class Container:
    cpu = 0
    memory_mb = 0
    storage_mb = 0
    name = ""
    performance_slowdown = 0.2
    colocation_factor = 0.1

    def __init__(self, name: str, cpu: float, memory_mb: int, storage_mb: int):
        self.name = name
        self.cpu = cpu
        self.memory_mb = memory_mb
        self.storage_mb = storage_mb

    def __repr__(self):
        return f"Container.{self.name}({self.cpu}, {self.memory_mb}, {self.storage_mb})"
