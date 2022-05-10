x=input("enter the first no")
x=int(x)
y=input("enter the second no.")
y=int(y)
z=input("enter the third no.")
z=int(z)
if (x>y and y>z):
  print(x,"is greatest no.")
elif (y>x and y>z):
  print(y,"is greatest no.")
else:
  print(z,"is greatest no.")
