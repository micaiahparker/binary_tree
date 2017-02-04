class NullNode:
    def __init__(self, parent):
        self.parent = parent

    def add(self, key, value):
        self.parent.grow(key, value)

    def search(self, key):
        return None

    def get_list(self):
        return list()

class LeftNullNode(NullNode):
    def add(self, key, value):
        self.parent.grow_left(key, value)

class RightNullNode(NullNode):
    def add(self, key, value):
        self.parent.grow_right(key, value)

class Node(NullNode):
    def __init__(self, parent, key, value):
        super().__init__(parent)
        self.key = key
        self.left_node = LeftNullNode(self)
        self.right_node = RightNullNode(self)

    def grow_left(self, key, value):
        self.left_node = Node(self, key, value)

    def grow_right(self, key, value):
        self.right_node = Node(self, key, value)

    def get_list(self):
        return self.left_node.get_list()+[self.key]+self.right_node.get_list()

    def add(self, key, value):
        if self.key > key:
            self.left_node.add(key, value)
        if self.key < key:
            self.right_node.add(key, value)

    def search(self, key):
        if self.key == key:
            return self
        if self.key > key:
            return self.left_node.search(key)
        if self.key < key:
            return self.right_node.search(key)
        return None
