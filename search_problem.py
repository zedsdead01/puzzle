from abc import ABCMeta, abstractmethod

__author__ = "Jan Kurcius"


class SearchProblem(metaclass=ABCMeta):
    @abstractmethod
    def get_children(self, state):
        ...

    @abstractmethod
    def is_goal(self, state):
        ...

    @abstractmethod
    def get_hashable(self, state):
        ...