with open("datoteka.txt", "a+") as dat:
    dat.write("water\n")
    dat.seek(0, 0)
    print(dat.readlines())



