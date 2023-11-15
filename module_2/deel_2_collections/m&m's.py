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
legezak = []

hoeveel = antwoord("hoeveel M&M's wil je in je zakje? ")

for i in range(hoeveel):
    kleur = random.choice(kleuren)
    legezak.append(kleur)
print(legezak)