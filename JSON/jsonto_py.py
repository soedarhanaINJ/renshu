#import from json to python
import json

#some JSON
x = '{ "name": "JOe Biden", "age": 23, "kuni": "Japans"}'

#pharse x:
y = json.loads(x) #mengambil data variable x(JSON) kemudian dibuat menjadi object python

#the result is a python dictionary
print(y["kuni"])