from abc import ABC, abstractmethod


class ITeacher(ABC):
    """Describes a teacher. Has fields: name(str), surname(str), patronymic(str), db(DataBase), code(int)"""
    @property
    @abstractmethod
    def name(self):
        """Getter gor name"""
        pass

    @property
    @abstractmethod
    def surname(self):
        """Getter for surname"""
        pass

    @property
    @abstractmethod
    def patronymic(self):
        """Getter for patronymic"""
        pass

    @property
    @abstractmethod
    def code(self):
        """Getter for code"""
        pass

    @property
    @abstractmethod
    def db(self):
        """Getter for db"""
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        """Setter for name"""
        pass

    @surname.setter
    @abstractmethod
    def surname(self, surname):
        """Setter for surname"""
        pass

    @patronymic.setter
    @abstractmethod
    def patronymic(self, patronymic):
        """Setter for patronymic"""
        pass

    @code.setter
    @abstractmethod
    def code(self, code):
        """Setter for code"""
        pass

    @db.setter
    @abstractmethod
    def db(self, db):
        """Setter for db"""
        pass

    @abstractmethod
    def __str__(self):
        """Returns string of object"""
        pass

