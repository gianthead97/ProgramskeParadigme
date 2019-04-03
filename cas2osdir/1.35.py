import os


path = raw_input ("Unesite putanju do direktorijuma: ")

i_duze = 0
i_sire = 0



for (trenutni, _, datoteke) in os.walk(path):
    for datoteka in datoteke:
        with open(os.path.join(trenutni, datoteka), "r") as f:
                sadrzaj = f.readlines()
                max_duzina_linije = 0
                broj_linija = 0
                for linija in sadrzaj:
                    broj_linija += 1
                    max_duzina_linije = max(max_duzina_linije, len(linija))

                if max_duzina_linije < broj_linija:
                    i_duze += 1
                else:
                    i_sire += 1


print("Kardinalnost skupa duze {}. Kardinalnost skupa sire {}.".format(i_duze, i_sire))

