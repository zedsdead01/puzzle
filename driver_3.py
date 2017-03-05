import sys
from puzzle import Puzzle
from uninformed_search import UninformedSearch
from queue import Queue
from stack import Stack
from tree import TreeNode
from collections import deque

__author__ = "Jan Kurcius"

if __name__ == '__main__':
    # Check if all script parameters have been specified.
    if len(sys.argv) < 3:
        print('Usage:\n\tpython3 driver_3.py <search_method> <initial_sequence>')
        exit()

    # Map each search method to the appropriate container class.
    containers = {
        'bfs': Queue,
        'dfs': Stack
    }

    # Create a container for the specified search method.
    search_method = sys.argv[1]
    assert search_method in containers.keys()
    container = containers[search_method]()

    # Create an initial sequence.
    start_state = Puzzle.State('start', list(map(lambda x: int(x), sys.argv[2].split(','))))
    assert len(start_state.tiles) == 9

    # Create an 8 by 8 puzzle board.
    puzzle = Puzzle()

    # Create a search object.
    search = UninformedSearch(puzzle, start_state, container)

    # Run the search.
    goal_node = search.run()
    assert isinstance(goal_node, TreeNode)

    path_to_goal = deque()
    node = goal_node
    while node.parent is not None:
        path_to_goal.appendleft(node.state.move)
        node = node.parent

    print(path_to_goal)
