from collections import Counter
import math, random

# Voorbeeld van het gebruik van de functie:

def Alle_getallen():
    aantal = len(getallenlijst)

    return aantal

def Gemiddelde_berekenen(som, aantal):
    gemiddelde = som / aantal

    return gemiddelde

def Opsomming_alle_getallen():
    som = sum(getallenlijst)

    return som

def Grootste_getal():
    grootste_getal = max(getallenlijst)

    return(grootste_getal)

def Kleinste_getal():
    kleinste_getal = min(getallenlijst)

    return(kleinste_getal)

def Eerste_getal():
    eerste_getal = getallenlijst[0]

    return(eerste_getal)

def kleingetal_deel_door_controlegetal1():
    delen1 = Kleinste_getal() / controlegetal1

    return delen1

def Grootstegetal_deel_door_controlegetal2():
    delen2 = Grootste_getal() / controlegetal2

    return delen2

def Unieke_getallen():
    unieke_getallen = list(set(getallenlijst))

    return unieke_getallen

def Aantal_unieke_elementen():
    aantal_unieke_elementen = len(Unieke_getallen())

    return aantal_unieke_elementen

def Verschil_tussen_uniek_en_controlegetal1():
    verschil1 = abs(Aantal_unieke_elementen() - controlegetal1)

    return verschil1

def Gesorteerde_lijst():
    gesorteerde_lijst = sorted(getallenlijst)

    return gesorteerde_lijst

def Unieke_gesorteerde_lijst():
    gesorteerde_lijst_uniek = sorted(Unieke_getallen())

    return gesorteerde_lijst_uniek

def Tel_unieke_getallen():
    telling_elementen = {}
    for getal in getallenlijst:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer

    return telling_elementen

def Deelbaar1_door_controlegetal1():
    deelbaar1 = []
    for getal in Unieke_getallen():
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)

    return deelbaar1

def Deelbaar2_door_controlegetal2():
    deelbaar2 = []
    for getal in Unieke_getallen():
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)

    return deelbaar2

def Bepaald_getal_controle():
    komtvoor = controlegetal1 in getallenlijst and controlegetal2 in getallenlijst

    return komtvoor

def Positie_eerste_controlegetal():
    posities = []
    for index, num in enumerate(getallenlijst):
        if num == controlegetal1:
            posities.append(index)

    return posities

def Standaard_afwijking_berekenen():
    verschil_kwadraat = sum((x - Gemiddelde_berekenen(Opsomming_alle_getallen(), Alle_getallen())) ** 2 for x in getallenlijst)
    variantie = verschil_kwadraat / Alle_getallen()
    standaardafwijking = math.sqrt(variantie)

    return standaardafwijking

def Shuffle_lijst():
    return random.shuffle(getallenlijst)

def Random_getal():
    random_getal = getallenlijst[random.randint(0,Alle_getallen()-1)]

    return random_getal

def Verschil_tussen_getallen(getal):
    verschil2 = abs(getal - controlegetal2)

    return verschil2

def Dict_maken():
    randomgetal = Random_getal()
    functiedict = {
        "Aantalgetallen": Alle_getallen(),
        "opsommen": Opsomming_alle_getallen(),
        "gemiddelde": Gemiddelde_berekenen(Opsomming_alle_getallen(), Alle_getallen()),
        "grootstegetal": Grootste_getal(),
        "kleinstegetal": Kleinste_getal(),
        "eerstegetal in de lijst": Eerste_getal(),
        "deelsom1": kleingetal_deel_door_controlegetal1(),
        "deelsom2":Grootstegetal_deel_door_controlegetal2(),
        "unieke elementen": Aantal_unieke_elementen(),
        "verschil":Verschil_tussen_uniek_en_controlegetal1(),
        "Gesorteerde lijst getallen": Gesorteerde_lijst(),
        "Gesorteerde lijst unieke getallen": Unieke_gesorteerde_lijst(),
        "Telling van elementen": Tel_unieke_getallen(),
        "Deelbaar1 controlegetal1": Deelbaar1_door_controlegetal1(),
        "Deelbaar2 door controlegetal2": Deelbaar2_door_controlegetal2(), 
        "controlegetal1 & controlegetal2": Bepaald_getal_controle(),
        "controlegetal1 positie(s)": Positie_eerste_controlegetal(),
        "Standaardafwijking": Standaard_afwijking_berekenen(),
        "Geshufflede lijst": Shuffle_lijst(),
        "Willekeurige getal": randomgetal,
        "verschil tussen random_getal & controlegetal2": Verschil_tussen_getallen(randomgetal)
        }
    
    resultaten = {
        "Aantal getallen": functiedict["Aantalgetallen"],
        "Gemiddelde":functiedict["gemiddelde"],
        "Som": functiedict["opsommen"],
        "Grootste getal": functiedict["grootstegetal"],
        "Kleinste getal": functiedict["kleinstegetal"],
        "Eerste getal": functiedict["eerstegetal in de lijst"],
        f"{functiedict['kleinstegetal']} / {controlegetal1}": functiedict["deelsom1"],
        f"{functiedict['grootstegetal']} / {controlegetal2}": functiedict["deelsom2"],
        "Aantal unieke elementen": functiedict["unieke elementen"],
        f"Het verschil tussen {functiedict['unieke elementen']} & {controlegetal1}": functiedict["verschil"],
        "Gesorteerde lijst getallen": functiedict["Gesorteerde lijst getallen"],
        "Gesorteerde lijst unieke getallen": functiedict["Gesorteerde lijst unieke getallen"],
        "Telling van elementen": functiedict["Telling van elementen"],
        f"Deelbaar door {controlegetal1} (op volgorde)": functiedict["Deelbaar1 controlegetal1"],
        f"Deelbaar door {controlegetal2} (op volgorde)": functiedict["Deelbaar2 door controlegetal2"],
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": functiedict["controlegetal1 & controlegetal2"],
        f"{controlegetal1} komt voor op positie(s)": functiedict["controlegetal1 positie(s)"],
        "Standaardafwijking": functiedict["Standaardafwijking"],
        "Geshufflede lijst": ["Geshufflede lijst"],
        "Willekeurige getal uit de lijst": functiedict["Willekeurige getal"],
        f"Het verschil tussen {functiedict['Willekeurige getal']} & {controlegetal2}": functiedict["verschil tussen random_getal & controlegetal2"],
    }
    return resultaten

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = dict_maken()
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
     print(f"{key}: {value}")