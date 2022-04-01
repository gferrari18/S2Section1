
class Student:
    def __init__(self, name="", ID=-1, birthdate="01/01/1995"):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate
    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        print('Wait, what?')


stud = Student()
stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

stud1 = Student()
stud1.name = "Gus"
stud1.ID = 12345
stud1.birthdate = "12/12/1995"

stud2 = Student()
stud2.name = "jeff"
stud2.ID = 18374
stud2.birthdate = "12/09/1995"

stud3 = Student()
stud3.name = "Matheuz"
stud3.ID = 1837
stud3.birthdate = "12/09/1895"

stud4 = Student()
stud4.name = "Hue"
stud4.ID = 187124
stud4.birthdate = "12/09/1993"

stud5 = Student("Mahoe", 15432, "12/31/1998")
stud6 = Student("Maloki", 12432, "12/10/3123")

class Teacher:
    def __init__(self, name="", ID=-1, birthdate="12/12/12",SME="",favoritecolor="",td=""):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate
        self.SME = SME
        self.favoritecolor = favoritecolor
        self.td = td
    def teach(self):
        print(self.name + " is teaching " + self.SME + ".")

    def ans(self):
        print("Well, maybe you should try it")

t1 = Teacher()
t1.name = "Monte"
t1.ID = 18342
t1.birthdate = "14/32/14"
t1.favoritecolor = "black"
t1.td = "difficult"

class Course:
    def __init__(self, students = [], subject = "", teacher = Teacher()):
        self.students = []
        self.subject = "Computer Science"
        self.teacher = Teacher()
    def enlist(self, x):
        self.students.append(x)
    def sub(self):
        print("This is a " + self.subject + " course.")
    def roster(self):
        for x in self.students:
            print(x.name)
    def getstudcount(self):
        return len(self.students)

c1 = Course()
c1.students = [stud,stud1,stud2,stud3,stud4]
c1.subject = "Counter Strike, how to get out of silver"

c1.teacher = t1
for s in c1.students:
    if s.name.startswith('M'):
        print(s.name)


t1.teach()
c1.roster()

for x in c1.students:
    print(x.name + " says: ")
    x.ask_question()

