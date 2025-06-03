def number(n):
    if (n== 0):
        return 0
    return n + number(n-1)

n = int(input("Enter a Number: "))
print(number(n))