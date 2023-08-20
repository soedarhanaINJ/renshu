#The findall() function returns a list containing all matches.
import re

txt = "Hujan turun di Japans"
x = re.findall("an", txt) #to find some text or word on txt variable. the syntax format is
#- re.findall('word what u wanna find', variable)

print(len(x))