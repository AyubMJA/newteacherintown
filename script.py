from roster import student_roster
import itertools

class Students:
    def __init__(self, studentList):
        self.studentsList = studentList

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(student_roster):
            student_status = self.studentsList[self.index]
            self.index += 1
            return student_status
        else:
            raise StopIteration

student_cls = Students(student_roster)
students_iter = iter(student_cls)

print(student_cls)
print(students_iter)
