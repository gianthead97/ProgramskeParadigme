import json

with  open("tacke.json", "r") as f:
    tacke = json.load(f)

for tacka in tacke:
    print (tacka["teme"])




sortirane_tacke = sorted(tacke, key = lambda x: x['koordinate'][0]**2 + x['koordinate'][1]**2)


for tacka in sortirane_tacke:
    print (tacka["teme"])
