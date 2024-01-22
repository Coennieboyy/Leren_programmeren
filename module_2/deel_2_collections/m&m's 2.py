import random

def antwoord(a):
    while True:
        getal = input(a)
        try:
            getal = int(getal)      
            return getal
        except ValueError:
            print(f"{getal} is geen getal, vul een getal in")

kleuren = ("orangje","blauw","groen","bruin")
bagofMnMs = {}

hoeveel = antwoord("hoeveel M&M's wil je in je zakje? ")

for i in range(hoeveel):
    kleur = random.choice(kleuren)
    if kleur in bagofMnMs:
        bagofMnMs[kleur] += 1
    else:
        bagofMnMs.update({kleur: 1})
print(bagofMnMs)