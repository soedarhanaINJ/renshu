set_ini = {'Cirebon', 'Subang', 'Hekinan'}
set2 = {'mangga', 'pisang', 'anggur', 'semangka'}
set_ini.remove('Hekinan') #remove item on set item. sesitive case
#-if Hekinan does not exist, .remove() will showing error.

set2.discard('Pisng') #if item on set2 does not exist, .discard() will NOT raise an error. different
#- .remove() and .discard() is on excecution!


print(set_ini)
print(set2)