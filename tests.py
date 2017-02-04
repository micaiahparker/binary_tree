from binary_tree import Tree

test_inputs = [1, 2, -1, 3]

def test_tree_add():
    tree = Tree()
    for key in test_inputs:
        tree.add(key, "sample_data")

    assert sorted(test_inputs) == tree.get_list()

def test_search_has():
    tree = Tree()
    for key in test_inputs:
        tree.add(key, "sample_data")

    for key in test_inputs:
        assert tree.search(key).key == key

def test_search_has_not():
    tree = Tree()
    for key in test_inputs:
        tree.add(key, "sample_data")

    assert tree.search(4) is None
