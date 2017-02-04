from binary_tree import Tree

test_inputs = [1, 2, -1, 3]

def test_tree():
    tree = Tree()
    for value in test_inputs:
        tree.add(value)

    assert sorted(test_inputs) == tree.get_list()
