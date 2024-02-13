import random

lijst1 = []

def antwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = str(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul text in")

while True:
    deelnemers = antwoord("voeg een deelnemer naam toe ")
    if deelnemers not in lijst1:
        lijst1.append(deelnemers)
    else:
        print("je naam zit al in de lijstjestrekker")

    if len(lijst1) >= 3:
        meerdeelnemers = antwoord("wil je nog meer deelnemers toevoegen? ")
        if meerdeelnemers == "nee" or meerdeelnemers == "n":
            lijst2 = lijst1.copy()
            break

poging = 0
while True:
    poging += 1
    dict = {}
    random.shuffle(lijst2)
    for num in range(len(lijst1)):
        if lijst1[num] != lijst2[num]:
            dict.update({lijst1[num]: lijst2[num]})
    if len(dict) == len(lijst1):
        print(dict, poging)
        break


     