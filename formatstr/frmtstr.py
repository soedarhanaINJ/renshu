#bagian penggabungan string dan number
umur = 23 #type data integer/int
txt = 'Hallo saya Soedarhana umur {}' #type data string

print(txt.format(umur))

#note int dan string tidak dapat disatukan kecuali dengan beberapa syarat contohnya .format()
"""
pengguanan .format() menempatkan nilai variable [umur = '23'(type int)] didalam kurung kurawal {} 
dan kurung kurawal {} disini ditempatkan di dalam variable txt(yang merupakan variable dengan type string)
"""