"""
A variable is only available from inside the region it is created. This is called scope.
"""

def my_function():
    x = 704 #local scope
    print(x)

my_function()