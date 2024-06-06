from functions import *
from data import *

print("Welkom bij Papi Gelato")

while nogEenKeer:
    opnieuw = True
    while opnieuw:
        opnieuw = False
        aantalBolletjes = hoeveelIjs()
        welkeSmaak(aantalBolletjes, ijsjesdict)
        hoorntjeOfBakjeStr = hoorntjeOfbakjeFunctie(aantalBolletjes)
        topping(hoorntjeOfBakjeStr)
    nogEenKeer = meerIjsjes(hoorntjeOfBakjeStr, aantalBolletjes)


bon(ijsjesdict)
print("Bedankt en tot ziens!")
 