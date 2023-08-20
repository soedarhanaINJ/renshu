car = {
"brand": "Ford", #first item . the Key is 'brand' . the value is 'Ford'
"model": "Mustang", #2nd item . the Key is 'model' . the value is 'Mustang'
"year": 1964 #3rd item . the Key is 'year' . the value is '1964'
}

x = car.items()

print(x) #before the change

car["year"] = 2020

car['color'] = 'black'

print(x) #after the change