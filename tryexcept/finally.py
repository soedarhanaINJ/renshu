"""
The finally block, if specified, will be executed regardless if the try block raises an error or not.
"""

try:
    print("Hello")

except:
    print("something went wrong")

finally:
    print("the 'Try Except' is finished")