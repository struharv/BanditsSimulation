import json

from engine.Container import Container
from engine.ElectricNode import ElectricNode


class InfrastructureLoader:

    @staticmethod
    def load(filename: str):
        nodes = []
        containers = []

        with open(filename) as f:
            doc = json.load(f)

            for node in doc["nodes"]:
                name = node["name"]
                cpu = node["cpu"]
                memory = node["memory"]
                storage = node["storage"]

                newNode = ElectricNode(name, cpu, memory, storage, [])
                nodes += [newNode]

            for container in doc["containers"]:
                name = node["name"]
                cpu = node["cpu"]
                memory = node["memory"]
                storage = node["storage"]

                newContainer = Container(name, cpu, memory, storage)
                containers += [newContainer]

            print(doc)
            print(nodes, containers)
            return nodes, containers




