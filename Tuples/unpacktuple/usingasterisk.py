"""
jika nilai varible kamu kurang dari nilai dari item yang tersedian kamu bisa gunakan asterisk
tambahkan symbol * dinama variable kamu, dan akan dimasukan ke variable sebagai list
"""
buah = ('apel', 'cherry', 'pisang', 'semangka', 'melon', 'ichigo') #variable buah yg memiliki 6 item

(green, yellow, *blue) = buah #ada 3 variable warna disini, dan variable blue menggunakan symbol asterisk
#- jika symbol asterisk (*) disimpan divariable yellow, maka semua item sembelum ichigo akan masuk ke list yellow
#- maka tampilan printnya akan seperti ini
# *yellow ['cherry', 'pisang', 'semangka', 'melon']
# blue [ichigo]

print(green)
print(yellow)
print(blue) #menampilkan variable blue yang itemnya lebih dari satu