"""
nilai item dari sebuah tuple bisa diubah,
"""

x = ('apel', 'semangka', 'kersem', 'buahnaga')
y = list(x) #memastikan item x sama dengan item y
y[1] = 'kiwi' #tambahkan kedalam item x yaitu buah 'kiwi' dengan otomatis mengganti nilai sebelumnya yang ada dituple x
x = tuple(y) #membuat tuple y dari sebuah tuple x ini adalah type tuple constructor

print(x)