class mobil:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Drive!')

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Sail!')

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Fly!')

car1 = mobil('BMW', 'Jupiter')
boat1 = boat('Ibiza', 'Touring20')
plane1 = plane('Boeing', '77')

for x in (car1, boat1, plane1):
    x.move()