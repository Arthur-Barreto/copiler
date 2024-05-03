from abc import ABC, abstractmethod


class Node(ABC):
    id_counter = 0

    def __init__(self, value: any, children: list):
        self.value = value
        self.children = children

    def get_id(self):
        Node.id_counter += 1
        return Node.id_counter

    @abstractmethod
    def evaluate(self, symbol_table):
        pass
