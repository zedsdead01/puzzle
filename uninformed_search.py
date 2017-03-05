from search_problem import SearchProblem
from search_container import Container
from tree import TreeNode

__author__ = "Jan Kurcius"


class UninformedSearch:
    def __init__(self, search_problem, state, container):
        assert isinstance(search_problem, SearchProblem)
        assert isinstance(container, Container)

        # Keep search problem and container object for later use.
        self.search_problem = search_problem
        self.fringe = container

        # Create a set of visited nodes and add the current state to it.
        self.visited = set()
        self.visited.add(self.search_problem.get_hashable(state))

        # Create a root tree node and add it to the fringe.
        self.current_node = TreeNode(None, state)
        self.fringe.put_one(self.current_node)

    def run(self):
        while True:
            # Stop searching if the fringe is empty.
            if self.fringe.size() == 0:
                break

            # Take the next element from the fringe
            self.current_node = self.fringe.take()
            assert isinstance(self.current_node, TreeNode)
            state = self.current_node.state

            # Check if the goal has been reached.
            if self.search_problem.is_goal(state):
                break

            # Get the children states of the current search state.
            successors = self.search_problem.get_children(state)

            # Generate hashable value for each of the children states.
            successors = list(map(lambda s: [s, self.search_problem.get_hashable(s)], successors))

            # Filter out those children states which have been already visited.
            successors = list(filter(lambda s: s[1] not in self.visited, successors))

            # Expand the current search tree node.
            child_nodes = []
            for child_state, hashable in successors:
                child_node = self.current_node.add_child(child_state)
                child_nodes.append(child_node)
                self.visited.add(hashable)

            # Add the children nodes to the fringe.
            self.fringe.put_many(child_nodes)

        return self.current_node
