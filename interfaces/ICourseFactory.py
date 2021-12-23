from abc import ABC, abstractmethod
from interfaces import iOffsiteCourse, iLocalCourse


class ICourseFactory(ABC):
    """Interface for factory which creates courses"""

    @property
    @abstractmethod
    def teachers(self):
        """Getter for teachers"""
        pass

    @property
    @abstractmethod
    def courses(self):
        """Getter for courses"""
        pass

    @property
    @abstractmethod
    def db(self):
        """Getter for db"""
        pass

    @abstractmethod
    def find_course(self, code):
        """Checks for duplicates in courses"""
        pass

    @abstractmethod
    def find_teacher(self, code):
        """Checks for duplicates in teachers"""
        pass

    @abstractmethod
    def create_local_course(self, teacher_code, course_code) -> iLocalCourse:
        """Method for creating local course"""
        pass

    @abstractmethod
    def create_offsite_course(self, teacher_code, course_code) -> iOffsiteCourse:
        """Method for creating offsite course"""
        pass
