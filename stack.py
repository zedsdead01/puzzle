from search_container import Container
from collections import deque

__author__ = "Jan Kurcius"


class Stack(Container):

    def __init__(self):
        self.stack = deque()

    def put_one(self, item):
        self.stack.appendleft(item)

    def put_many(self, items):
        items.reverse()

        for item in items:
            self.stack.appendleft(item)

    def take(self):
        return self.stack.popleft()

    def size(self):
        return len(self.stack)