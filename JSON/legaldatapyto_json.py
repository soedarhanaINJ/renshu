import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=". ", sort_keys=True)) #Use the indent parameter to define the numbers of indents
#or showing real syntax position
#separators="" You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:

#sort_key= type is boolean the meaning is True or False for sorted parameter