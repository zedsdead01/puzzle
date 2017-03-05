from search_container import Container
from collections import deque

__author__ = "Jan Kurcius"


class Queue(Container):

    def __init__(self):
        self.queue = deque()

    def put_one(self, item):
        self.queue.append(item)

    def put_many(self, items):
        self.queue += items

    def take(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)