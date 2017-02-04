from .node import Node, NullNode

class Tree:
    def __init__(self):
        self.root = NullNode(self)

    def add(self, key, value):
        self.root.add(key, value)
        return self

    def search(self, key):
        return self.root.search(key)

    def grow(self, key, value):
        self.root = Node(self, key, value)

    def get_list(self):
        return self.root.get_list()
