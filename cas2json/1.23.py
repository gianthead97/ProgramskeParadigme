import json


f = open("datoteka.json", "r")

x = json.load(f)

print(x["Ime"])
print(x["Prezime"])
print(x["Godine"])


f.close()