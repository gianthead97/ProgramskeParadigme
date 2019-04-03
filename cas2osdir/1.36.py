import os
import json


path = raw_input("Unesite putanju do direktorijuma: ")

ekstenzije = {}

for (trenutni, roditelj, datoteke) in os.walk(path):
    for datoteka in datoteke:
        print (datoteka)
        indeks = datoteka.rfind(".")
        eks = datoteka[indeks:]
        if eks in ekstenzije.keys():
                ekstenzije[eks] += 1
        else:
                ekstenzije[eks] = 1

with open("rezultati.json", "w") as f:
        json.dump(ekstenzije, f)


