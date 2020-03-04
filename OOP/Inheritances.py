class Person:
    def __init__(self, name):
        self.name = name
    def print(self):
        print("Person class")

class Teacher(Person):
    def __init__(self, name, level):
        super(Teacher, self).__init__(name)
        self.level = level

    def print(self):
        print("Teacher class")

    def print_parent(self):
        super(Teacher, self).print()


teacher = Teacher('ali', 12)
print(teacher.name)
print(teacher.level)
teacher.print()
teacher.print_parent()