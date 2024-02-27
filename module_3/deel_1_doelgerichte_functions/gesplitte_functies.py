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

print(f"Aantal getallen: {alle_getallen(getallenlijst)}")
print(f"opsommen: {opsomming_alle_getallen(getallenlijst)}")
print(f"gemiddelde: {gemiddelde_berekenen(opsomming_alle_getallen(getallenlijst), alle_getallen(getallenlijst))}")
print(f"grootste getal: {grootste_getal(getallenlijst)}")
