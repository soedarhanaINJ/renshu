"""
The function will print the local x, and then the code will print the global x:
"""

x = 1909 #this is global scope

def my_function():
    x = 6835
    print(x) #first print is 6835, this is local scope

my_function()

print(x)