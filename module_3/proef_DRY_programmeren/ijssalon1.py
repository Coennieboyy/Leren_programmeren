from functions import *
from data import *


print("Welkom bij Papi Gelato")

klant = soortKlant()


while nogEenKeer:
    aantalBolletjes = hoeveelIjs(klant)

    if klant:
        welkeSmaak(aantalBolletjes, ijsjesdict, antwoorddictSmaken, klant)
        hoorntjeOfBakjeStr = hoorntjeOfbakjeFunctie(aantalBolletjes)
        topping(hoorntjeOfBakjeStr,aantalBolletjes)
        nogEenKeer = meerIjsjes(hoorntjeOfBakjeStr, aantalBolletjes)
    else:
        welkeSmaak(aantalBolletjes, ijsjesdict, antwoorddictSmakenLiter, klant)
        nogEenKeer = False


if nogEenKeer == False:
    bon(ijsjesdict, klant) 
print("\nBedankt en tot ziens!")
 