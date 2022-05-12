'''def user_input():
   a,b=int(input("Enter value1:")),int(input("Enter value2:"))
   return(a,b)
def add(a,b):
   return a+b
a,b=user_input()
#add(a,b)c=add(a,b)
print(a,'+',b,'=',add(a,b))
'''
#local and global variable
count=1
def plus():
  global count
  count+=1
def minus():
  global count
  count-=1
print("count=",count)
plus()
plus()
minus()
minus()
print("count= ",count)


