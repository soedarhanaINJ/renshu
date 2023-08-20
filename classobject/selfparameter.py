class orang:
    def __init__(initeh, nama, gaji):
        initeh.nama = nama
        initeh.gaji = gaji

    def my_function(uye):
        print('Hello aenk teh ' + uye.nama )

nu1 = orang('IKEH', 230000)
nu1.gaji = 270000

nu1.my_function()
print('gaji aenk', nu1.gaji)
