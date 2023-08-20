harga = 69000

txt = "Harganya adalah {:.2f} Yen" #Format the price to be displayed as a number with two decimals
#- you can add just like txt = "Harganya adalah {} Yen" for deleting 2 decimal in the last price showed
print(txt.format(harga)) #The .format() method allows you to format selected parts of a string