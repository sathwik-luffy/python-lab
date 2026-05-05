class Student:

    def __init__(self):
        self.ro = None
        self.name = None

    def setData(self, ro, name):
        self.ro = ro
        self.name = name

    def putData(self):
        print("Roll No:", self.ro)
        print("Name:", self.name)


class Test(Student):

    def __init__(self):
        super().__init__()
        self.marks = [0, 0, 0]

    def getMarks(self, marks):
        self.marks = marks

    def putMarks(self):
        print(f"Marks are {self.marks}")


class Sports:

    def __init__(self):
        self.score = None

    def getScore(self, score):
        self.score = score

    def putScore(self):
        print("Score:", self.score)


class Result(Test, Sports):

    def __init__(self):
        Test.__init__(self)
        Sports.__init__(self)
        self.avg = 0

    def display(self):
        self.avg = (sum(self.marks) / len(self.marks)) + self.score

        print("Average:", self.avg)

        if self.avg >= 40:
            print("Pass")
        else:
            print("Fail")


obj = Result()

obj.setData(101, "John")
obj.getMarks([70, 80, 90])
obj.getScore(5)

obj.putData()
obj.putMarks()
obj.putScore()
obj.display()