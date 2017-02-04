from .node import Node, NullNode

class Tree:
    def __init__(self):
        self.root = NullNode(self)

    def add(self, value):
        self.root.add(value)

    def grow(self, value):
        self.root = Node(self, value)

    def get_list(self):
        return self.root.get_list()
