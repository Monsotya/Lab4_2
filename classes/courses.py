from interfaces.iCourse import ICourse
from classes.teacher import Teacher
from classes.dataBase import DataBase


class Course(ICourse):
    """Class that describes courses"""
    def __init__(self, teacher, course, db):
        """Constructor for course:
        @:param course(int) - course, @:param teacher(int/Teacher) - teacher, @:param db(DataBase) - data base)"""
        self.__name = None
        self.__topics = None
        self.__db = db
        self.teacher = teacher
        self.code = course

    @property
    def topics(self):
        """Getter for topics"""
        return self.__topics

    @topics.setter
    def topics(self, topics):
        """Setter for topics"""
        if not isinstance(topics, str):
            raise TypeError
        if not topics:
            raise ValueError

        self.__topics = topics

    @property
    def db(self):
        """Getter for name"""
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

        courses = self.__db.get_courses()
        for course in courses:
            if course[0] == code:
                self.name = course[1]
                self.topics = course[2]
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
    def teacher(self):
        """Getter for teacher"""
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        """Setter for teacher"""
        if isinstance(teacher, int):
            if teacher < 1:
                raise TypeError
            self.__teacher = Teacher(teacher, self.__db)
        if isinstance(teacher, Teacher):
            self.__teacher = teacher