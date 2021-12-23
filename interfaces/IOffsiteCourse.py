from abc import ABC, abstractmethod


class IOffsiteCourse(ABC):
    """Class for offsite course"""
    @abstractmethod
    def __str__(self):
        """Returns string of object"""
        pass
