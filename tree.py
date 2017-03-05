__author__ = "Jan Kurcius"

class TreeNode:
    def __init__(self, parent, val):
        self.parent = parent
        self.state = val
        self.children = []

    def add_child(self, state):
        child_node = TreeNode(self, state)
        self.children.append(child_node)
        return child_node

    def add_children(self, states):
        assert isinstance(states, list)
        state_nodes = list(map(self.add_child, states))
        self.children += state_nodes
        return state_nodes
