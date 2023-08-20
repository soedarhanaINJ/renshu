"""
The sub() function replaces the matches with the text of your choice:
"""

#Replace every white-space character with the number 7:
import re

txt = "The rain in Spain"
x = re.sub("\s", "7", txt)

print(x)