class student():
    institution="IIPS"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("------------------------")
        print("marks in python=",self.a)
        print("marks in python lab=",self.b)
        print("------------------------")
    @classmethod
    def info(self):
        print("class belongs to",self.institution)
    @staticmethod
    def about():
        print("this class hold the data of marks obtained by ")

s1=student(12,16)
s2=student(13,11)
s3=student(14,9)
s1.show()
s2.show()
student.info()
student.about()


