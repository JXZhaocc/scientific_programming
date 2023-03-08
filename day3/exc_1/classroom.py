class Person:
    def __init__(self,first_name, family_name) -> None:
        self.first_name = first_name
        self.last_name = family_name
    
    def print_name(self):
        return print(self.first_name , self.last_name)
    
class Student(Person):
    def __init__(self,first_name, family_name, subject) -> None:
        super(Student,self).__init__(first_name, family_name)
        self.subject = subject

    def printNameSubject(self):
        return print(self.first_name, self.last_name, self.subject)

class Teacher(Person):
    def __init__(self, first_name, family_name, course_name) -> None:
        super().__init__(first_name, family_name)
        self.course_name = course_name

    def printNameCourse(self):
        return print(self.first_name, self.last_name, self.course_name)

