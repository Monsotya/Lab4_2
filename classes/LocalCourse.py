from interfaces.iLocalCourse import ILocalCourse
from classes.courses import Course


class LocalCourse(ILocalCourse, Course):
    """Class that describes local course"""
    def __str__(self):
        """Returns string of an object"""
        return f'Local course: {self.name}, teacher: {self.teacher}, program topics: {self.topics}'