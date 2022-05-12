#factorial program
num=int(input("Enter the number"))
if(num<0):
   print("factorial not exist for negative numbers")
elif(num==0):
   print("The factorial of 0 is 1")
else:
  fact=1
  for i in range(1,num+1):
      fact=fact*i;
print("factorai is=",fact)
