from abc import ABCMeta, abstractmethod

__author__ = "Jan Kurcius"


class Container(metaclass=ABCMeta):
    @abstractmethod
    def put_one(self, item):
        ...

    @abstractmethod
    def put_many(self, items):
        ...

    @abstractmethod
    def take(self):
        ...

    @abstractmethod
    def size(self):
        ...
