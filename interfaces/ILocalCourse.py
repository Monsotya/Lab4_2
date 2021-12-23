from abc import ABC, abstractmethod


class ILocalCourse(ABC):
    """Interface for local course"""
    @abstractmethod
    def __str__(self):
        """Returns string of object"""
        pass
