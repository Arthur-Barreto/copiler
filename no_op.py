from node import Node


class NoOp(Node):
    def __init__(self):
        super().__init__(None, [])
        # Node.get_id()

    def evaluate(self, symble_table):
        pass
