from abc import ABC, abstractmethod


class Counter:
    id = 0


class Node(ABC):

    def __init__(self, value: any, children: list):
        self.value = value
        self.children = children
        self.id = Counter.id
        Counter.id += 1

    @abstractmethod
    def evaluate(self, symbol_table):
        pass
