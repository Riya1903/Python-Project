year=int(input("Enter year to find it is leap year or not: "))

if(year%400==0):
        print("The year is leap year!!")
elif(year%100==0 ):
            print(" The year is not leap year!")
elif(year%4==0 ):
            print(" The year is leap year!")
            
else:
        print("The year is not leap year!")
