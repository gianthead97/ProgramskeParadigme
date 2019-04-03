import os

print (os.listdir(os.curdir))
for (trenutni_dir, poddirektorijumi, datoteke) in os.walk(os.curdir):
    print (trenutni_dir)
    for datoteka in datoteke:
        print (os.path.join(trenutni_dir, datoteka))
