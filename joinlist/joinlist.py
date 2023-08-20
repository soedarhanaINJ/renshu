"""
Cara mudah untuk menggabungkan beberapa item dalam dua/++ variable
adalah dengan menggunakan operator +
"""
list = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list + list2 #gabungkan 2 variable list & list2

"""
Cara lain untuk menambakan item dalam variable adalah dengan syntax .append()
"""
kota = ['Bandung', 'Subang', 'Cirebon', 'Tasik']
kota_2 = ['Jepang', 'Australia']
for x in kota_2: #x disini adalah item dalam variable kota_2
    kota.append(x) #u/ kota tambahkan item x (item kota_2) kedalam index kota

"""
Cara lainnya adalah bisa menggunakan syntax .extend()
"""

tanggal = [27, 19, 7, 5]
olddate = [30, 31]
tanggal.extend(olddate) #gunakan syntax .extend() untuk menambahkan 2 variable
tanggal.sort() #.sort() untuk menuyusun numeric (0-9)

print(list3)
print(kota)
print(tanggal)