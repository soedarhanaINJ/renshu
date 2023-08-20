class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def my_function(self):
        print('Hello my name is ' + self.nama)

p1 = Person('Dilan', 17)
p1.my_function()

#The self parameter is a reference to the current instance of the class,
#- and is used to access variables that belong to the class.