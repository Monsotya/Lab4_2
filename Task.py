from classes.courseFactory import CourseFactory

if __name__ == '__main__':
    obj = CourseFactory("C:\\Users\\Sophia\\Documents\\GitHub\\Lab4_2\\Courses.db")
    print("Enter:\n0 - to add new course with teacher\n1 - to look at all the teachers\n2 - to look at all the courses"
          "\n3 - to exit")
    ind = int(input())
    while ind != 3:
        if not ind:
            print("Enter teacher code")
            teacher_code = int(input())
            print("Enter course code")
            course_code = int(input())
            print("0 - local course\n1 - offsite course")
            number = int(input())
            if not number:
                obj.create_local_course(teacher_code, course_code)
            elif number == 1:
                obj.create_offsite_course(teacher_code, course_code)

        elif ind == 1:
            for teacher in obj.teachers:
                print(teacher)

        elif ind == 2:
            for course in obj.courses:
                print(course)

        print("Enter:\n0 - to add new course with teacher\n1 - to look at all the teachers"
              "\n2 - to look at all the courses\n3 - to exit")
        ind = int(input())
