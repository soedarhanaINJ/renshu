"""
Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().
"""

tupleini = ('apel', 'pisang', 'chery', 'semangka')
iniiterator = iter(tupleini)

print(next(iniiterator))
print(next(iniiterator))
print(next(iniiterator))
print(next(iniiterator))