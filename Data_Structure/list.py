name = ["mosh", "juthi", "sarah", "john"]
print(name[0:-1])
# maximumnumber in a list
number = [2, 3, 4, 56, 7, 22, 45]
max = number[0]
for n in number:
    if n > max:
        max = n
print(f"maximum number:{max}")
# ------2d list-----
matrix = [[1, 2, 3], [4, 5, 6]]

print(matrix[1][1])  # '5'
# accessing each item in a 2d list
for r in matrix:
    for c in r:
        print(c)
# list method
print("the list we are working on:\n", number)
number.append(10)
print("append an item in the end:\n", number)
number.insert(0, 1)
print("insert an item in the given index:\n", number)
number.remove(10)
print("remove the given item:\n", number)
number.pop()
print("remove the last item:\n", number)
print("return the index of the given item(4):\n", number.index(4))
print("checking the existance of an item(50)in the list:\n", 50 in number)
print("the number of occurance of an item(2) in the list:\n", number.count(2))
number.sort()
print("the sorted list in ascending order:\n", number)
number.reverse()
print("the sorted list in descending order:\n", number)
number2 = number.copy()
number.clear()
print(f"the copied list:\n{number2} \nthe original  cleared list:\n{number}")
