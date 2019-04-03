try:
    with open("datoteka.txt", "r") as datoteka:
        for linija in datoteka:
            print(linija)
except IOError:
    print("Nije uspelo otvaranje datoteke")


