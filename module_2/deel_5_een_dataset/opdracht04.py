from fruitmand import fruitmand
import random

def intantwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = int(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul een integer in")


aantal = intantwoord("Hoeveel fruit? ")
fruitmand2 = {}
for i in range(aantal):
    fruit = random.choice(fruitmand)
    print(fruit['name'])
    if fruit['name'] in fruitmand2:
        fruitmand2[fruit['name']] += 1
    else:
        fruitmand2.update({fruit["name"]: 1})

print(fruitmand2)