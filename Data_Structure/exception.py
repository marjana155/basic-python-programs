from timeit import timeit
# how to work with exception
try:
    # how to workwith files
    with open("app.py") as file, open("list.py") as file1:
        print(" two file have opened")
    age = int(input("enter your age:"))
    age = 10/age
except(ValueError, ZeroDivisionError):
    print("You didn't enter valid age")
else:
    print("no exception was thrown")
# raising excption


code1 = """
def x_factor(age):
    if age <= 0:
        raise ValueError("age can not be less than or equal zero")
    return 10/age


try:
    x_factor(-1)
except ValueError as error:
    pass
"""
code2 = """
def x_factor(age):
    if age <= 0:
        return None
    return 10/age



if x_factor(-1)== None:
    pass

"""
print("first code:", timeit(code1, number=10000))
print("second code:", timeit(code2, number=10000))
