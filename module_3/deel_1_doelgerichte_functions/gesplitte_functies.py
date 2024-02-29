from collections import Counter
import math, random

# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
#analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
# print("Analyse resultaten:")
# for key, value in analyse_resultaat.items():
#     print(f"{key}: {value}")

def alle_getallen(getallenlijst):
    aantal = len(getallenlijst)

    return aantal

def gemiddelde_berekenen(som, aantal):
    gemiddelde = som / aantal

    return gemiddelde

def opsomming_alle_getallen(getallenlijst):
    som = sum(getallenlijst)

    return som

def grootste_getal(getallenlijst):
    grootste_getal = max(getallenlijst)

    return(grootste_getal)

def kleinste_getal(getallenlijst):
    kleinste_getal = min(getallenlijst)

    return(kleinste_getal)

def Eerste_getal(getallenlijst):
    eerste_getal = getallenlijst[0]

    return(eerste_getal)

def kleingetal_deel_door_controlegetal1(controlegetal1):
    delen1 = kleinste_getal(getallenlijst) / controlegetal1

    return delen1

def Grootstegetal_deel_door_controlegetal2(controlegetal2):
    delen2 = grootste_getal(getallenlijst) / controlegetal2

    return delen2

def Unieke_getallen(getallenlijst):
    unieke_getallen = list(set(getallenlijst))

    return unieke_getallen

def Aantal_unieke_elementen(getallenlijst):
    aantal_unieke_elementen = len(Unieke_getallen(getallenlijst))

    return aantal_unieke_elementen

def Verschil_tussen_uniek_en_controlegetal1(getallenlijst):
    verschil1 = abs(Aantal_unieke_elementen(getallenlijst) - controlegetal1)

    return verschil1

def Gesorteerde_lijst(getallenlijst):
    gesorteerde_lijst = sorted(getallenlijst)

    return gesorteerde_lijst

def Unieke_gesorteerde_lijst(getallenlijst):
    gesorteerde_lijst_uniek = sorted(Unieke_getallen(getallenlijst))

    return gesorteerde_lijst_uniek

def Tel_unieke_getallen(getallenlijst):
    telling_elementen = {}
    for getal in getallenlijst:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer

    return telling_elementen

def Deelbaar1_door_controlegetal1(getallenlijst):
    deelbaar1 = []
    for getal in Unieke_getallen(getallenlijst):
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)

    return deelbaar1

def Deelbaar2_door_controlegetal2(getallenlijst):
    deelbaar2 = []
    for getal in Unieke_getallen(getallenlijst):
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)

    return deelbaar2

def Bepaald_getal_controle(getallenlijst):
    komtvoor = controlegetal1 in getallenlijst and controlegetal2 in getallenlijst

    return komtvoor

def Positie_eerste_controlegetal(getallenlijst):
    posities = []
    for index, num in enumerate(getallenlijst):
        if num == controlegetal1:
            posities.append(index)

    return posities

def Standaard_afwijking_berekenen(getallenlijst):
    verschil_kwadraat = sum((x - gemiddelde_berekenen(opsomming_alle_getallen(getallenlijst), alle_getallen(getallenlijst))) ** 2 for x in getallenlijst)
    variantie = verschil_kwadraat / alle_getallen(getallenlijst)
    standaardafwijking = math.sqrt(variantie)

    return standaardafwijking

def Shuffle_lijst(getallenlijst):
    return random.shuffle(getallenlijst)

def random_getal(getallenlijst):
    random_getal = getallenlijst[random.randint(0,alle_getallen(getallenlijst)-1)]

    return random_getal

def verschil_tussen_getallen(getallenlijst):
    verschil2 = abs(random_getal(getallenlijst) - controlegetal2)

    return verschil2

print(f'''Aantal getallen: {alle_getallen(getallenlijst)}
opsommen: {opsomming_alle_getallen(getallenlijst)}
gemiddelde: {gemiddelde_berekenen(opsomming_alle_getallen(getallenlijst), alle_getallen(getallenlijst))}
grootste getal: {grootste_getal(getallenlijst)}
kleinste getal: {kleinste_getal(getallenlijst)}
eerste getal in de lijst: {Eerste_getal(getallenlijst)}
{kleinste_getal(getallenlijst)} / {controlegetal1}: {kleingetal_deel_door_controlegetal1(controlegetal1)}
{grootste_getal(getallenlijst)} / {controlegetal2}: {Grootstegetal_deel_door_controlegetal2(controlegetal2)}
Aantal unieke elementen: {Aantal_unieke_elementen(getallenlijst)}
Het verschil tussen {Aantal_unieke_elementen(getallenlijst)} & {controlegetal1}: {Verschil_tussen_uniek_en_controlegetal1(getallenlijst)}
Gesorteerde lijst getallen: {Gesorteerde_lijst(getallenlijst)}
Gesorteerde lijst unieke getallen: {Unieke_gesorteerde_lijst(getallenlijst)}
Telling van elementen: {Tel_unieke_getallen(getallenlijst)}
Deelbaar door {controlegetal1} (op volgorde): {Deelbaar1_door_controlegetal1(getallenlijst)}
Deelbaar door {controlegetal2} (op volgorde): {Deelbaar2_door_controlegetal2(getallenlijst)}
{controlegetal1} & {controlegetal2} komt wel voor in de lijst {Bepaald_getal_controle(getallenlijst)}
{controlegetal1} komt voor op positie(s) {Positie_eerste_controlegetal(getallenlijst)}
Standaardafwijking: {Standaard_afwijking_berekenen(getallenlijst)}
Geshufflede lijst: {Shuffle_lijst(getallenlijst)}
Willekeurige getal uit de lijst: {random_getal(getallenlijst)}
Het verschil tussen {random_getal(getallenlijst)} & {controlegetal2}: {verschil_tussen_getallen(getallenlijst)}''')
