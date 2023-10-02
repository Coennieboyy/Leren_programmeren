print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("|                 SOLICITATIE circus directeur                 |")
print("|                                                              |")
print("|     Er worden een aantal nodige vragen gesteld.              |")
print("|     Graag hebben we datt u dat eerlijk invuld.               |")
print("|     Als u voldoet aan de benodigdheden,                      |")
print("|     Zullen we u uitnodigen voor een solicitatie gesprek.     |")
print("|                           Succes!                            |")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

jalist = ("ja" , "j" , "JA" , "J")
neelist = ("nee" , "n" , "NEE" , "N")
fouten = []
GLIMLACH = 10
KRULHAAR = 20
SNOR = 10
WERKNEMERS = 5
ONDERNEMER = 3
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 240
DIERENERVARING = 4
JONGLEERERVARING = 5
PRAKTIJKERVARING = 3


rijbewijs = input("heb je een geldig vrachtwagen rijbewijs? J/N ")
if rijbewijs not in jalist:
    fouten.append("je hebt nog geen rijbewijs.")
hogehoed = input("ben je in bezit van een hogehoed? J/N ")
if hogehoed not in jalist:
    fouten.append("je mist een grote hoed")
gewicht = float(input("hoe zwaar ben je? "))
if gewicht not in jalist:
    fouten.append("Uw gewicht voldoet niet aan onze eisen.")
lengte = float(input("hoelang ben je? "))
if lengte not in jalist:
    fouten.append("UW lengte voldoet niet aan onze eisen.")
certificaat = input("heb je het certificaat: “Overleven met gevaarlijk personeel”? J/N ")
if certificaat not in jalist:
    fouten.append("je hebt geen certificaat.")
dierenervaring = float(input("hoelang heb je ervaring met dieren of dressuur? "))
if dierenervaring not in jalist:
    fouten.append("je hebt niet lang genoeg ervaring met dieren.")
jongleerervaring = float(input("hoelang heb je ervaring met jongleren? "))
if jongleerervaring not in jalist:
    fouten.append("je hebt niet lang genoeg ervaring met jongleren.")
praktijkervaring = float(input("hoelang heb je ervaring met acrobatiek? "))
if praktijkervaring not in jalist:
    fouten.append("je hebt niet lang genoeg ervaring met acrobatiek.")

diploma = input("heb je een MBO-4 diploma? J/N ")
if diploma not in jalist:
        ondernemertijd = float(input("hoelang ben je ondernemer? Als je geen ervaring heb als ondernemer voer 0 in. "))
        if ondernemertijd > 0:
            werknemers = int(input("hoeveel werknemers heb je in loondienst? als je geen ervaring heb als ondernemer voer 0 in. "))
            if ondernemertijd < ONDERNEMER:
                fouten.append("u hebt niet genoeg ervaring als ondernemer")
                if diploma not in jalist and ondernemertijd < ONDERNEMER and werknemers < WERKNEMERS:
                    fouten.append("u hebt geen diploma MBO-4")
                    fouten.append("u hebt niet genoeg ervaring als ondernemer")
                    fouten.append("u hebt te weinig werknemers")

    

geslacht = input("ben je een man of vrouw of anders? ")
if geslacht == "man":
    snor = (input("heb je een snor? J/N "))
    if snor in jalist:
        lengtesnor = int(input("hoelang is je snor in cm? "))
        if lengtesnor <= 10:
            fouten.append("je snor is te kort.")

elif geslacht == "vrouw":
    krulhaar = (input("hebt u rood krul haar? J/N "))
    if krulhaar in jalist:
        lengtekrulhaar = int(input("hoelang is je haar in cm? "))
        if lengtekrulhaar < 20:
            fouten.append("je haar is te kort.")
elif geslacht == "anders":
    smile = int(input("hoe groot is je glimlach in cm?"))
    if smile < 10:
        fouten.append("je glimlach is te smal")

if fouten == []:
    ("gefeliciteerd u bent uitgenodigd voor een solicitatie gesprek!")
else:
    print("Sorry u komt niet in aanmerking: U ontbreekt de volgende criteria: ")
for i in fouten:
    print(i)