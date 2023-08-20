fruits = ['banana', 'apple', 'semangka', 'melon']
newfruits = [x.upper() for x in fruits] #item sama dengan variable fruits, tapi dengan huruf kapital semua

#tambahkan value dari variable fruits
newfruits2 = ['Ini' for x in fruits]

newfruits3 = [x if x != 'banana' else 'Jeruk' for x in fruits]
#jika item bukan banana kembalikan ke item asli, tapi jika item ada banana maka ganti dengan jeruk

print(newfruits)
print(newfruits2)
print(newfruits3)