from abc import ABC, abstractmethod


class ICourse(ABC):
    """Interface that describes courses"""

    @property
    @abstractmethod
    def name(self):
        """Getter for name"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """Getter for teacher"""
        pass

    @property
    @abstractmethod
    def topics(self):
        """Getter for topics"""
        pass

    @property
    @abstractmethod
    def db(self):
        """Getter for db"""
        pass

    @db.setter
    @abstractmethod
    def db(self, db):
        """Setter for db"""
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        """Setter for name"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """Setter for teacher"""
        pass

    @topics.setter
    @abstractmethod
    def topics(self, topics):
        """Setter for topics"""
        pass
