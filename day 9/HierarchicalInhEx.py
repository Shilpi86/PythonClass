# hierarchical : from one class to multiple classes

class Teacher:
    def English(self):
        print("2 subjects in English")

class Student1(Teacher):
    def option1(self):
        print("1st period- Literature")

class Student2(Teacher):
    def option2(self):
        print("2nd period - Language")

a = Student1()
b = Student2()
a.English()
b.English()
a.option1()
b.option2()



