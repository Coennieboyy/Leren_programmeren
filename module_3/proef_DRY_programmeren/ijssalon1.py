from functions import *
from data import *

print("Welkom bij Papi Gelato")

while nogEenKeer:
    aantalBolletjes = hoeveelIjs()
    welkeSmaak(aantalBolletjes, ijsjesdict)
    hoorntjeOfBakjeStr = hoorntjeOfbakjeFunctie(aantalBolletjes)
    topping(hoorntjeOfBakjeStr,aantalBolletjes)
    nogEenKeer = meerIjsjes(hoorntjeOfBakjeStr, aantalBolletjes)


bon(ijsjesdict)
print("Bedankt en tot ziens!")
 