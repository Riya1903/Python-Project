

class calculation():
    
    def area(self,para1=None,para2=None):
        if(para1!=None and para2!=None):
           x=para1*para2
           return x;
        elif(para1!=None and para2==None):
           x=3.14*para1*para1
           return x;
        else:
            x="NO parameters passed"
            return x
y=calculation()
rectangle=y.area(12,3)
circle=y.area(12)
circle=round(circle,2)
print("Area of rectangle:",rectangle)
print("Area of circle:",circle)


 
    
