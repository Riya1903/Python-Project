class student():
    
    def avg(self,a=None,b=None,c=None):
       
        if(a!=None and b!=None and c!=None):
            average=a+b+c/3
            return average
        elif(a!=None and b!=None and c==None):
            average=a+b/2
            return average
        elif(a!=None and b==None and c==None):
         average=a
        else:
         average="No values provided"
      
s1=student()
avg1=s1.avg(12,24,16)
avg2=s1.avg(54,12)
avg3=s1.avg(12)
avg4=s1.avg()
print(avg2)
print(avg3)
print(avg4)
