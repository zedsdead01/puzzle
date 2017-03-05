from search_problem import SearchProblem

__author__ = "Jan Kurcius"


class Puzzle(SearchProblem):
    class State:
        def __init__(self, move, tiles):
            self.move = move
            self.tiles = tiles

    def __init__(self):
        up = 'up'
        down = 'down'
        left = 'left'
        right = 'right'

        self.children = {
            0: [down, right],
            1: [down, left, right],
            2: [down, left],
            3: [up, down, right],
            4: [up, down, left, right],
            5: [up, down, left],
            6: [up, right],
            7: [up, left, right],
            8: [up, left]
        }

        self.offsets = {
            up: -3,
            down: 3,
            left: -1,
            right: 1
        }

        self.goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def get_children(self, state):
        assert isinstance(state, Puzzle.State)
        zero_index = state.tiles.index(0)
        return list(map(lambda move: Puzzle.State(move, self.move_sequence(move, state.tiles[:])), self.children[zero_index]))

    def move_sequence(self, direction, sequence):
        zero_index = sequence.index(0)
        if direction in self.children[zero_index]:
            new_index = zero_index + self.offsets[direction]
            sequence[zero_index] = sequence[new_index]
            sequence[new_index] = 0
        else:
            print("WARNING: Impossible move.")

        return sequence

    def is_goal(self, state):
        assert isinstance(state, Puzzle.State)
        if state.tiles == self.goal:
            return True
        else:
            return False

    def get_hashable(self, state):
        assert isinstance(state, Puzzle.State)
        return ''.join(list(map(lambda val: str(val), state.tiles)))
