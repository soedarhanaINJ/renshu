#RegEx or Regular Expressions
import re

txt = "Hujan turun di Japans"
x = re.search("^Hujan.*Japans$", txt)

if x:
    print("Yes")
else:
    print("No Match")