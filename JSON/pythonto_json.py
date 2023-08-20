import json

#a python object dict
x = {
    "nama": "Joe Viden",
    "umur": 23,
    "kuni": "Japans"
}

#convert int0 JSON:
y = json.dumps(x) #create python object to JSON

#the result is a JSON string
print(y)