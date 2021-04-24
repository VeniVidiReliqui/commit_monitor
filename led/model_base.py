"""
"""
import abc

class LedModel(metaclass=abc.ABCMeta):
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = None
        self.initialize()

    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def get_grid(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass
    