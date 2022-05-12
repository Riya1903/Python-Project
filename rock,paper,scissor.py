#rock,paper and scissor game
u1=int(input("user one choice(rock,paper,scissor):"))
u2=int(input("user two choice(rock,paper,scissor):"))

print(" 1 means rock")
print(" 2 means paper")
print("3 means scissor")

if(u1==1):
    if(u2==1):
        print("it's tie")
    if(u2==3):
        print("user 1 wins!")
    if(u2==2):
        print("user 2 won!")

elif(u1==2):
    if(u2==1):
        print("use one won!")
    if(u2==3):
        print("user 2 wins!")
    if(u2==2):
        print("it's tie!")
elif(u1==3):
    if(u2==1):
        print("user 2 won")
    if(u2==3):
        print("tie!")
    if(u2==2):
        print("user 1 won!")
else:
     print("you enter rong choice")


    

