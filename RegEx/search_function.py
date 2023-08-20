import re

txt = "The rain in the Spains"
x = re.search("\s", txt)

print("The first white-space is located in posx`ition: ", x.start())