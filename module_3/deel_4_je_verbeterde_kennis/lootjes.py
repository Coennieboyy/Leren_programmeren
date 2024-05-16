import random

lijst1 = []
dictCadeau = {

}

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
        for i in range(3):
            cadeau = input("wat voor cadeau's wil je? ")
            if deelnemers not in dictCadeau:
                dictCadeau.update({deelnemers:[cadeau]})
            else:
                dictCadeau[deelnemers].append(cadeau)
            
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
        break



while True: 
    naamvragen = input("van wie wil je het lootje weten? ")
    getrokkenPersoon = dict[naamvragen]
    if naamvragen in dict:
        print(f"Hallo {naamvragen} jij hebt {getrokkenPersoon} getrokken")
        print(f"het verlanglijstje van {getrokkenPersoon} is {dictCadeau[getrokkenPersoon]}")
        break
    else:
        print(f"Die naam zit er niet in, kies uit {lijst1}")