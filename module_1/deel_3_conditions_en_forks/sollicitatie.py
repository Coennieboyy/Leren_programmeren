print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("|             solicitatie circus directeur            |")
print("|                                                     |")
print("|Er worden een aantal nodige vragen gesteld.          |")
print("|Graag hebben we datt u dat eerlijk invuld.           |")
print("|Als u voldoet aan de benodigdheden,                  |")
print("|Zullen we u uitnodigen voor een solicitatie gesprek. |")
print("|Succes!                                              |")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


rijbewijs = input("heb je een geldig vrachtwagen rijbewijs? J/N ")
hogehoed = input("ben je in bezit van een hogehoed? J/N ")
gewicht = int(input("hoe zwaar ben je? "))
lengte = float(input("hoelang ben je? "))
certificaat = input("heb je het certificaat: “Overleven met gevaarlijk personeel”? J/N ")
dierenervaring = float(input("hoelang heb je ervaring met dieren of dressuur? "))
jongleerervaring = float(input("hoelang heb je ervaring met jongleren? "))
praktijkervaring = float(input("hoelang heb je ervaring met acrobatiek? "))
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 240
DIERENERVARING = 4
JONGLEERERVARING = 5
PRAKTIJKERVARING = 3
jalist = ("ja" , "j" , "JA" , "J")
neelist = ("nee" , "n" , "NEE" , "N")


if rijbewijs in jalist and hogehoed in jalist and (gewicht > MIN_WEIGHT and gewicht < MAX_WEIGHT) and (lengte > MIN_LENGTE and lengte < MAX_LENGTE) and certificaat in jalist and (dierenervaring >= DIERENERVARING) and (jongleerervaring >= JONGLEERERVARING) and (praktijkervaring >= PRAKTIJKERVARING):
    print("je bent aangenomen! ")
else:
    print("je bent niet aangenomen:( ")