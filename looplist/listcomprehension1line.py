kota = ['Bandung', 'Subang', 'Jakarta', 'Cirebon']

newkota = [x for x in kota if 'u' in x] #bentuk sederhana dari file listcomprehension.py
#newlist = [expression for item in iterable if condition == True]
#hasilnya menampilkan variable newkota, tanpa mengubah item variable kota
kota2 = [x for x in kota if x != 'Bandung'] #hanya menerima item yang bukan "Bandung"
kota3 = [x for x in range(7) if x < 5] #total index ada 7, tampilkan semua index yang kurang dari 5

print(newkota)
print(kota2)
print(kota3)