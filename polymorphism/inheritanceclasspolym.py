class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Drive')

class Car(Vehicle):
    pass

class boat(Vehicle):
    def move(self):
        print('Sail')

class plane(Vehicle):
    def move(self):
        print('Fly!')

car1 = Car('BMW', 'Jupiter')
boat1 = boat('Ibiza', 'Touring20')
plane1 = plane('Boeing', '77')

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()