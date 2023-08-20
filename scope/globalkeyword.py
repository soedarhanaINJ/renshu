"""
If you use the global keyword, the variable belongs to the global scope:
"""

def my_function():
    global x #this syntax will create variable x to global scope
    x = 704 #local scope, buttt

my_function()

print(x)