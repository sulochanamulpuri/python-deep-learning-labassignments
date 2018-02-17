class system(object): #1st class
    def __init__(self):
        self.instnme = input("enter your institution name")
        print("institution name:", self.instnme)

class Person(object):#2ndclass

    def __init__(self):
        self.name = ""

        self.age = 0

    def get(self):
        self.name = input("Enter the Name:")

        self.age = int(input("Age?"))

    def disp(self):
        print("Name :", self.name, "\t Age :", self.age)


class Student(Person): #3rd class and inheritance from person
    avg = int(input("Average?"))

    def __init__(self):
        super(Student, self).__init__() #superclass

        self.rollno = 0

        self.avg = 0.0
        _gender = 15 #privatemember

    def readStudent(self):
        # Call get method of parent class

        super(Student, self).get()

        self.rollno = int(input("Enter the Roll Number:"))

    def disprollno(self):
        print("Roll No. :", self.rollno)


class GradStudent(Student): #4th class and multilevel inheritance

    def __init__(self):
        super(Student, self).__init__()

        self.subject = ""

        self.working = ""

    def readGrad(self):
        # Call readStudent method of parent class

        super(Student, self).readStudent()

        self.subject = input("Enter subject of graduation")

        self.working = input("Working? y/n")

    def workstatus(self):
        return self.working

    def displaysubject(self):
        print("Subject:", self.subject)


class grades(system, Student):  #5th class and multiple inheritance
    def __init__(self):
        super(Student, self).__init__()
        super(system, self).__init__()
        self.grade = 0

    def gradest(self):
        y = Student.avg
        if (y > 80):
            print("grade=A")
        elif (y in range(70, 80)):
            print("grade=B")
        else:
            print("grade=C")

s=system()  #instantiation
p=Person()
p.get()
p.disp()
st=Student()
st.readStudent()
st.disprollno()
hu=grades()
hu.gradest()




