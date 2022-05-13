class Test():
    def __init__(self,subject1,subject2):
        self.subject1=subject1
        self.subject2=subject2
    def show(self):
        print(self.subject1)
        print(self.subject2)
    def __add__(self,other):
        subject1=self.subject1+other.subject1
        subject2=self.subject2+other.subject2
        return Test(subject1,subject2)
t1=Test(21,17)
t2=Test(18,17)
t3=t1+t2
t3.show()
