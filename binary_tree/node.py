class NullNode:
    def __init__(self, parent):
        self.parent = parent

    def add(self, value):
        self.parent.grow(value)

    def get_list(self):
        return list()

class LeftNullNode(NullNode):
    def add(self, value):
        self.parent.grow_left(value)

class RightNullNode(NullNode):
    def add(self, value):
        self.parent.grow_right(value)

class Node(NullNode):
    def __init__(self, parent, value):
        super().__init__(parent)
        self.value = value
        self.left_node = LeftNullNode(self)
        self.right_node = RightNullNode(self)

    def grow_left(self, value):
        self.left_node = Node(self, value)

    def grow_right(self, value):
        self.right_node = Node(self, value)

    def get_list(self):
        return self.left_node.get_list()+[self.value]+self.right_node.get_list()

    def add(self, value):
        if self.value > value:
            self.left_node.add(value)
        if self.value < value:
            self.right_node.add(value)
