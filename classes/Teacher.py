from interfaces.iTeacher import ITeacher
from classes.dataBase import DataBase


class Teacher(ITeacher):
    """Class that describes teacher"""
    def __init__(self, code, db):
        """Constructor for teacher @:param code(int) - code of teacher, @:param db(DataBase) - database)"""
        self.__name = None
        self.__surname = None
        self.__patronymic = None
        self.db = db
        self.code = code

    def __str__(self):
        """Returns string of an object"""
        return f'{self.__name} {self.__surname} {self.__patronymic}'

    @property
    def db(self):
        """Getter for db"""
        return self.__db

    @db.setter
    def db(self, db):
        """Setter for db"""
        if not isinstance(db, DataBase):
            raise TypeError

        self.__db = db

    @property
    def code(self):
        """Getter for code"""
        return self.__code

    @code.setter
    def code(self, code):
        """Setter for code"""
        if not isinstance(code, int):
            raise TypeError
        if code < 1:
            raise ValueError

        teachers = self.__db.get_teachers()
        for teacher in teachers:
            if teacher[0] == code:
                self.name = teacher[1]
                self.surname = teacher[2]
                self.patronymic = teacher[3]
                break

        if not self.__name:
            raise ValueError
        self.__code = code

    @property
    def name(self):
        """Getter for name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Setter for name"""
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError

        self.__name = name

    @property
    def surname(self):
        """Getter for surname"""
        return self.__surname

    @surname.setter
    def surname(self, surname):
        """Setter for surname"""
        if not isinstance(surname, str):
            raise TypeError
        if not surname:
            raise ValueError

        self.__surname = surname

    @property
    def patronymic(self):
        """Getter for patronymic"""
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        """Setter for patronymic"""
        if not isinstance(patronymic, str):
            raise TypeError
        if not patronymic:
            raise ValueError

        self.__patronymic = patronymic









