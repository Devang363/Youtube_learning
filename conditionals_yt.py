a=int(input("Enter your age : "))

if (a >= 18):
    print("You are above the age of consent")
    print("Good for you")

elif (a<0):
    print("You are entering invalid age .\n Negative age doesn't exist")

elif (a==0):
    print("You Are Entering 0 Which Is Not Valid")

else : 
    print("You are below the age of consent")

print("End of program")
