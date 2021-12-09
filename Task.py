from abc import ABC, abstractmethod


class ILocalCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):

    @abstractmethod
    def create_local_course(self, name, teacher, program) -> ILocalCourse:
        pass

    @abstractmethod
    def create_offsite_course(self, name, teacher, program) -> IOffsiteCourse:
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def surname(self):
        pass

    @property
    @abstractmethod
    def patronymic(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @surname.setter
    @abstractmethod
    def surname(self, surname):
        pass

    @patronymic.setter
    @abstractmethod
    def patronymic(self, patronymic):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_course(self, course):
        pass


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @program.setter
    @abstractmethod
    def program(self, program):
        pass


class CourseFactory(ICourseFactory):
    def create_local_course(self, name, teacher, program) -> ILocalCourse:
        return LocalCourse(name, teacher, program)

    def create_offsite_course(self, name, teacher, program) -> IOffsiteCourse:
        return OffsiteCourse(name, teacher, program)


class Teacher(ITeacher):
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

        self.__courses = []

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__patronymic}'

    def add_course(self, course):
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError

        self.__courses.append(course)

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


class Course(ICourse):
    def __init__(self, name, teacher, program):
        self.name = name
        self.teacher = teacher
        self.program = program

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
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError

        teacher.add_course(self)
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not isinstance(program, list):
            raise TypeError
        if not program:
            raise ValueError
        if not all(isinstance(x, str) for x in program):
            raise TypeError
        if not all(x for x in program):
            raise ValueError

        self.__program = program


class LocalCourse(ILocalCourse, Course):
    def __str__(self):
        return f'Local course: {self.name}, teacher: {self.teacher}, program topics: {self.program}'


class OffsiteCourse(IOffsiteCourse, Course):
    def __str__(self):
        return f'Offsite course: {self.name}, teacher: {self.teacher}, program topics: {self.program}'


lecturer = Teacher("a", "b", "c")
obj = CourseFactory().create_local_course("aa", lecturer, ["programming", "oop"])
print(obj)