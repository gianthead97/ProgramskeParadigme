import random

print "----   IGRA: Ajnc   -----"


ime = raw_input("Unesite Vase ime: ")

print "Zdravo ", ime
znakovi = ("Karo", "Tref", "Pik", "Herc")
brojevi = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K")
karte = []

for znak in znakovi:
    for broj in brojevi:
        karte.append((znak, broj))

