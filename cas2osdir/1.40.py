with open("reci.txt", "r") as datoteka:
    sadrzaj = datoteka.readlines()

reci = []
for linija in sadrzaj:
    linija = linija.split(" ")
    for rec_tmp in linija:
        reci.append(rec_tmp)
#while "!" == rec = input():

while True:
    rec = input()
    if rec == "!":
        exit()
    for test in reci:
        if test.startswith(rec) == True:
            print (test)