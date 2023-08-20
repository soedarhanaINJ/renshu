f = open("demofile3.txt", "w")

f.write("Woops! i have delete the content")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())