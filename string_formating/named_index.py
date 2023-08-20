"""
You can also use named indexes by entering a name inside the curly brackets {mobil},
but then you must use names when you pass the parameter values txt.format(mobil = "kijang"):
"""

order = "I have  a {mobil}, it is a {model_mobil}"

print(order.format(mobil = "Kijang", model_mobil = "Hijau"))