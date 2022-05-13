num=int(input("Enter any number: "))
i=2
while(i<=num-1):
    if(num%i==0):
        print("number is not a prime")
        break
    else:
        print("number is prime")
        break
else:
    print("number is not prime")
