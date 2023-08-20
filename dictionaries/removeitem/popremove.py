mobil = {
    'model': 'kijang',
    'warna': 'private',
    'tahun': 1996,
    'nama_pemilik': 'dilan'
}

mobil.pop('warna') #.pop() you must choice or specified what item wanna remove
mobil.popitem() #.popitem() ini python before v 3.7 will remove randomly item

print(mobil)