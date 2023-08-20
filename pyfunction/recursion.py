def e_recursion(x):
    if (x > 0):
        result = x + e_recursion(x - 1)
        print(result)

    else :
        result = 0
    return result

print('\nRecursion Example Result') #syntax\n memerintahkan untuk membuat garis baru
e_recursion(7)