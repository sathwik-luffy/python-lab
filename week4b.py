class Student:

    def __init__(self):
        self.rollno = 0
        self.name = ""

    def getData(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def putData(self):
        print(f"Rollno: {self.rollno}")
        print(f"Name: {self.name}")


class Test(Student):

    def __init__(self):
        super().__init__()
        self.marks = [0, 0, 0]

    def getMarks(self, marks):
        self.marks = marks

    def putMarks(self):
        print(f"Marks are {self.marks}")


class Result(Test):

    def __init__(self):
        super().__init__()
        self.avg = 0

    def display(self):
        self.avg = sum(self.marks) / len(self.marks)

        print("Average:", self.avg)

        if self.avg >= 40:
            print("Pass")
        else:
            print("Fail")


obj = Result()

obj.getData(101, "John")
obj.getMarks([80, 75, 90])

obj.putData()
obj.putMarks()
obj.display()