from interfaces.iTeacher import ITeacher
from classes.dataBase import DataBase


class Teacher(ITeacher):
    """Class that describes teacher"""
    def __init__(self, code, db):
        self.__name = None
        self.__surname = None
        self.__patronymic = None
        self.db = db
        self.code = code

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__patronymic}'

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        if not isinstance(db, DataBase):
            raise TypeError

        self.__db = db

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
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
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError

        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        if not surname:
            raise ValueError

        self.__surname = surname

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError
        if not patronymic:
            raise ValueError

        self.__patronymic = patronymic









