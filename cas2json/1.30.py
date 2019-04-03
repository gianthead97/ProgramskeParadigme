import json


with open("dat1.txt", "r") as dat1:
    datoteka1 = dat1.readlines()

with open("dat2.txt", "r") as dat2:
    datoteka2 = dat2.readlines()



recnik = {}
dodato = False
for linija in datoteka1:
    if linija.lstrip() == "\n":
        pass

    recnik[linija.lstrip()] = 1

for linija in datoteka2:
    if linija.lstrip() == "\n":
        pass    
    if linija not in recnik.keys():
        recnik[linija.lstrip()] = 2
        dodato = True
    elif linija in recnik.keys() and recnik[linija.lstrip()] == 2:
        recnik[linija.lstrip()] = 2
    else:
        recnik[linija.lstrip()] += 2


razlike_u_prvom = 0
razlike_u_drugom = 0

for k, v in recnik.items():
    if v == 1:
        print ("Iz 1: " + k)
        razlike_u_prvom += 1
    elif v == 2:
        print ("Iz 2: " + k)
        razlike_u_drugom += 1


#print (razlike_u_prvom)
#print (razlike_u_drugom)

