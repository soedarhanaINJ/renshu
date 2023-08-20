class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
"""
if this syntax bellow not used, python will return the main. Person object
syntax bellow :
"""
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)