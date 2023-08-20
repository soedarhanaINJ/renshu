inituple = ('aple', 'banana', 'kersem', 'melon', 'manggis', 'semangka')
print(inituple[1]) #bisa mengakses tuple dengan menunjukan index dari sebuah item
print(inituple[-1]) #bisa akses nilai index dengan minus juga
print(inituple[2:5]) #range of index, pencarian dimulai dari index no 2 dimasukan/terhitung - index no 5 tapi
#- index no 5 tidak dimasukan/dihitung

if 'semangka' in inituple: #check apakah suatu item didalam nilai dari suatu tuple variable
    print("Yes, 'semangka' ada dituple ini")

#seperti biasa sebuah index dimulai dengan nilai dari [0]