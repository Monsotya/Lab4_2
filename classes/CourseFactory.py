from interfaces.iCourseFactory import ICourseFactory
from interfaces.iLocalCourse import ILocalCourse
from interfaces.iOffsiteCourse import IOffsiteCourse
from classes.offsiteCourse import OffsiteCourse
from classes.localCourse import LocalCourse
from classes.dataBase import DataBase


class CourseFactory(ICourseFactory):
    """Factory for creating local and offsite courses"""
    def __init__(self, path):
        """Constructor for course factory: @:param path(string) - path to data base)"""
        self.__courses = []
        self.__teachers = []
        self.__db = DataBase(path)

    @property
    def teachers(self):
        """Getter for teachers"""
        return self.__teachers

    @property
    def courses(self):
        """Getter for courses"""
        return self.__courses

    @property
    def db(self):
        """Getter for db"""
        return self.__db

    def find_teacher(self, code):
        """Checks for duplicates in teachers"""
        if not isinstance(code, int):
            raise TypeError
        if code < 1:
            raise ValueError
        for teacher in self.__teachers:
            if teacher.code == code:
                return teacher
        return False

    def find_course(self, code):
        """Checks for duplicates in courses"""
        if not isinstance(code, int):
            raise TypeError
        if code < 1:
            raise ValueError
        for course in self.__courses:
            if course.code == code:
                return course
        return False

    def create_local_course(self, teacher_code, course_code) -> ILocalCourse:
        """Method for creating local course"""
        if self.find_course(course_code) and self.find_teacher(teacher_code):
            if isinstance(self.find_course(course_code), LocalCourse):
                raise ValueError
        if self.find_teacher(teacher_code):
            obj = LocalCourse(self.find_teacher(teacher_code), course_code, self.__db)
            self.__courses.append(obj)
            self.__db.add_course_teacher(teacher_code, course_code, "Local course")
            return obj

        self.__db.add_course_teacher(teacher_code, course_code, "Local course")
        obj = LocalCourse(teacher_code, course_code, self.__db)
        self.__courses.append(obj)
        self.__teachers.append(obj.teacher)
        return obj

    def create_offsite_course(self, teacher_code, course_code) -> IOffsiteCourse:
        """Method for creating offsite course"""
        if self.find_course(course_code) and self.find_teacher(teacher_code):
            if isinstance(self.find_course(course_code), OffsiteCourse):
                raise ValueError
        if self.find_teacher(teacher_code):
            obj = OffsiteCourse(self.find_teacher(teacher_code), course_code, self.__db)
            self.__courses.append(obj)
            self.__db.add_course_teacher(teacher_code, course_code, "Offsite course")
            return obj

        self.__db.add_course_teacher(teacher_code, course_code, "Offsite course")
        obj = OffsiteCourse(teacher_code, course_code, self.__db)
        self.__courses.append(obj)
        self.__teachers.append(obj.teacher)
        return obj