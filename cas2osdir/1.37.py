import json
from datetime import datetime


def na_odmoru(radnik):
    if datetime.strptime(radnik["odmor"][0], "%d.%m.%Y.") < datetime.now() \
        < datetime.strptime(radnik["odmor"][1], "%d.%m.%Y."):
        return True
    else:
        return False


def u_radnom_vremenu(radnik):
    godina = datetime.now().year
    mesec = datetime.now().month
    dan = datetime.now().day

    pocetak_dana = datetime(godina, mesec, dan, int(radnik["radno_vreme"][0][:2]),\
         int(radnik["radno_vreme"][0][3:]))
    kraj_dana = datetime(godina, mesec, dan, int(radnik["radno_vreme"][1][:2]),\
        int(radnik["radno_vreme"][1][3:]))


    if pocetak_dana < datetime.now() < kraj_dana:
        return True
    else:
        return False

with open("radnici.json", "r") as f:
    radnici = json.load(f)


opcija = input("Unesite opciju koju zelite\nd-dostupni radnici\no-radnici na odmoru: ")


if opcija not in ("d", "o"):
    print("Nije podrzana opcija")
    exit()


for radnik in radnici:
    if opcija == "o" and na_odmoru(radnik):
        print (radnik["ime"])
    elif opcija == "d" and na_odmoru(radnik) == False and u_radnom_vremenu(radnik):
        print (radnik["ime"])

