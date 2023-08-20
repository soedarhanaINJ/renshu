""""
You can't remove item in a tuple

Note : Tuple is a unchangable, so you can't remove item on it, But you can use same workaround
like as w3school used.
"""

tupleini = ('Bandung', 'Cirebon', 'Majalengka', 'Inggris') #list tuple 'tupleini'
y = list(tupleini) #tampilkan item tuple 'tupleini' dan bentuk menjadi tuple y
y.remove('Majalengka') #list tuple y hapus item 'Majalengka'
tupleini = tuple(y) #tambahkan/or gabungkan tupleini dan tuple y

print(tupleini)

x = ('Ciremai', 'Arjuno', 'Lawu')
del x #delete semua item termasuk tuplenya, tpi akan menimmbulkan eror di hasil print

print(x)