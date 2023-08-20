"""
.sort() memfilter secara otomatis dari alphabet (a-z) / numeric (0-9)
tapi huruf kapital disalah satu item dalam variable juga berpengaruh ke sytax .sort() ini
huruf kapital akan dieksekusi pertama sebagai abjad paling kecil,
jika ada alphabet a dan A, maka syntax .sort() akan mengeksekusi A terlebih dahulu
"""
list = ['Banana', 'semangka', 'melon', 'Jambu']
list.sort() #.sort() peng-urutan alphabet, dari a-z dari KAPITAL ke huruf biasa

print(list)

list2 = ['banana', 'semangka', 'melon', 'jambu']
list2.sort(key = str.lower)

print(list2)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #.reverse() membalikan urutan item
print(thislist)
