class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 10

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Person:
    def greet(self):
        print("person greet")


class Employee:
    def greet(self):
        print("Employee greet")


class Manager(Employee, Person):
    pass


m = Mammal()
m.eat()
print(m.weight)
man = Manager()
man.greet()
