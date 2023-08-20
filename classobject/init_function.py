"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:
"""

class orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

p1 = orang('John', 17)

print(p1.nama)
print(p1.umur)

#The __init__() function is called automatically every time the class is being used to create a new object.