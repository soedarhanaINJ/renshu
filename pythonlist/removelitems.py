list = ['bear', 'inu', 'neko', 'sakana', 'doraemon']
list2 = ['anjing', 'beruang', 'monyet', 'babbi']
list3 = ['setang', 'genderewo', 'kuntai', 'poci']
list4 = ['bandung', 'subang', 'cirebon', 'tasik']
list.remove('bear') #.remove('') menghapus value dari variable bisa menggunakan .remove('')
list2.pop(2) #.pop() mengkhapus index dengan cara mencantumkan no indexnya saja
            #JIKA INDEXNYA DIKOSONGKAN MAKA AKAN OTOMATIS MENGHAPUS INDEX BAGIAN PALING AKHIR
del list3[1] #keyword del bisa digunakan untuk menghapus item index, dan harus diisi no index yg akan dihapus
            #keyword del juga bisa menghapus semua nilai variable menggunakan keyword " del 'variable' "
list4.clear() #.clear() menghapus nilai(isi variable)

print(list)
print(list2)
print(list3)
print(list4)