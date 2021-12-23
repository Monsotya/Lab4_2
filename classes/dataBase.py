from os.path import exists
import sqlite3
from sqlite3 import Error


class DataBase:
    """Class for getting and inserting information from data base"""
    def __init__(self, path):
        """Constructor for data base @:param path(str) - path to data base"""
        self.path = path
        self.connection = self.path

    def add_course_teacher(self, teacher_code, course_code, type_course):
        """Adds new course-teacher connection"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'INSERT INTO Course_Teacher (Course, Teacher, Type_of_course) VALUES  ({course_code},'
                           f'{teacher_code},"{type_course}");')
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")

    def get_teachers(self):
        """Returns all the teachers from data base"""
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * from Teacher")
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")

    def get_courses(self):
        """Returns all the courses from data base"""
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * from Course")
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, path):
        if not isinstance(path, str):
            raise TypeError
        if not path:
            raise ValueError
        if not exists(path):
            raise ValueError

        self.__connection = sqlite3.connect(path)

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        if not isinstance(path, str):
            raise TypeError
        if not path:
            raise ValueError
        if not exists(path):
            raise ValueError

        self.__path = path
