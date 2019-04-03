import os

for ime in os.listdir():
    if os.path.isfile(ime):
        print(os.path.abspath(ime))
