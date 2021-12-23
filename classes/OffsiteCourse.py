from interfaces.iOffsiteCourse import IOffsiteCourse
from classes.courses import Course


class OffsiteCourse(IOffsiteCourse, Course):
    """Class that describes offsite course"""
    def __str__(self):
        """Returns string of an object"""
        return f'Offsite course: {self.name}, teacher: {self.teacher}, program topics: {self.topics}'