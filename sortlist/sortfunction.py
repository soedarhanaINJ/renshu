def myFunction(n):
    return abs(n - 50) #abs (absolute) atau nilai yang mutlak

list = [100, 50, 63, 89, 69, 23]
list.sort(key = myFunction) #menjalankan list item dari kecil - besar, tapi dengan kata kunci variable 'myFunction'
#artinya dimulai dengan jumlah n-50. dan 50 sebagai patokan diawal

print(list)