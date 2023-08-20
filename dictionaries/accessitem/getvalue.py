car = {
"brand": "Ford", #first item . the Key is 'brand' . the value is 'Ford'
"model": "Mustang", #2nd item . the Key is 'model' . the value is 'Mustang'
"year": 1964 #3rd item . the Key is 'year' . the value is '1964'
}

x = car.values() #get the value only like a "Ford", "Mustang", 1964

print(x) #before the change

car["year"] = 2020 #add new value is 2020 with key is 'year'
#-if dictionaries have same key or value, the last add on dictionaries will show up!

car['color'] = 'white' #add new key (color) and value (white)

print(x) #after the change