def my_function(n):
    return lambda a : a * n #do 11 * 2

myduobler = my_function(2) #value n/ function n/ is 2.

print(myduobler(11)) #value a/ value lambda is 11