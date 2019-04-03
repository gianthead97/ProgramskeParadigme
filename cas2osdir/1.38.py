import os

datoteka = input("Unesi naziv datoteke: ")


for (trenutni, _, folder) in os.walk("//"):
    for fajl in folder:
        if (datoteka == fajl + ""):
            print (os.path.abspath(os.path.join(trenutni, fajl)))
            

