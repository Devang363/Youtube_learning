n = int(input("Enter a number : "))
i = 0
while(i < n):
    i+=1
    print(" "*(n-i) , end ="")
    print("*"* (2*i-1), end ="")
    print("") 