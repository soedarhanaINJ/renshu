quantity = 7
item_no = 704
price = 57963
my_order = 'Saya beli sebanyak {} atau item yang no {} dengan harga satu item {}' #susunan otomatis mengikuti varible
cb = 'Beli {1} harga {2} {0} buah' #pengindex-an dimulai dari 0 dihitung dari variable

print(my_order.format(quantity, item_no, price))
print(cb.format(quantity, item_no, price))


#.format () tidak memerlukan single or double quotes