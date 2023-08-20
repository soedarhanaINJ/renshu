"""
Cara menambahkan item kedalam tuple adalah salah satu caranya dengan cara mengubah tuple ke bentuk list
kemuadian tambahkan item kedalam list, terakhir kembalikan list kebentuk semula dalam bentuk tuple
"""

x = ('Bandung', 'Cirebon', 'Subang', 'Bali') #item variable x
y = list(x) #tampilkan list dari variable x dan buat variable bari dengan nama variable y
y.append('Medan') #.append u/ menambahkan item kedalam list y
x = tuple(y) #ubah kembali varible y ke x dengan tuple

print(x)