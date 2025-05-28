lst = []
for i in range(9):
    marks = int(input("Enter Marks : "))
    lst.append(marks)
    lst.sort()
print("Sorted Marks List:", lst)
n= lst.count(0)
print(n)

print(sum(lst))