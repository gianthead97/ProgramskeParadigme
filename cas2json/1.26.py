import json

def azurirajRacun(prodavnica, ime_voca):
    cena = 0
    for voce in prodavnica:
        if voce["ime"] == ime_voca:
            return voce["cena"]

f = open("korpa.json", "r")
korpa = json.load(f)
f.close()

f = open("maxi_cene.json", "r")
maxi_cene = json.load(f)
f.close()


f = open("idea_cene.json", "r")
idea_cene = json.load(f)
f.close()

f = open("shopngo_cene.json", "r")
shopngo_cene = json.load(f)
f.close()


maxi_racun = 0
idea_racun = 0
shopngo_racun = 0

i = 0
while i < len(korpa):
    maxi_racun += azurirajRacun(maxi_cene, korpa[i]["ime"]) * korpa[i]["kolicina"]
    idea_racun += azurirajRacun(idea_cene, korpa[i]["ime"]) * korpa[i]["kolicina"]
    shopngo_racun += azurirajRacun(shopngo_cene, korpa[i]["ime"]) * korpa[i]["kolicina"]



print(maxi_racun)
print(idea_racun)
print(shopngo_racun)




