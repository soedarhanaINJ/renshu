"""
Add a new item to the original dictionary, and see that the keys list gets updated as well:
"""

mobil = {
    'model': 'kijang',
    'warna': 'private',
    'tahun': 1996
}

x = mobil.keys() #.keys() take the "model", "warna", "tahun" only.

print(mobil)

mobil['color'] = 'black' #add key "color" to dictionaries mobil with value is 'black'

print(mobil)