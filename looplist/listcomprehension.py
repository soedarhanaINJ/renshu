list = ['Bandung', 'Subang', 'Cirebon', 'Tasik']
newlist = []

for x in list: #untuk item yang ada didalam variable list
    if 'a' in x: #jika ada huruf 'a' didalam variable list
        newlist.append(x) #masukan item yang ada huruf 'a' kedalam variable newlist[]

print(newlist)