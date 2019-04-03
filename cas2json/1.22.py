import json

ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
godine = int(input("Unesite godine: "))

junak = {"Ime": ime, "Prezime": prezime, "Godine": godine}
print(json.dumps(junak))


f = open("datoteka.json", "w")
json.dump(junak, f)
f.close()