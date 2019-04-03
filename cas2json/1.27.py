import json
from datetime import datetime

f = open("ispiti.json", "r")
ispiti = json.load(f)
f.close()


for ispit in ispiti:
    danas = datetime.now()
    datum_ispita = datetime.strptime(ispit["datum"], "%d.%m.%Y.")
    if danas < datum_ispita:
        print(ispit['ime'] + ": Prosao")
    else:
        print("Jos " + datum_ispita - danas + " dana")