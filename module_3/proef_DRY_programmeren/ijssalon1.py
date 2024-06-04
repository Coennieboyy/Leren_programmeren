from functions import *
from data import *

print("Welkom bij PapiGelato je mag alle smaken kiezen zo lang het maar vanilleijs is")

while nogEenKeer:
    opnieuw = True
    while opnieuw:
        opnieuw = False
        aantalBolletjes = hoeveelIjs()
        hoorntjeOfBakjeStr = hoorntjeOfbakjeFunctie(aantalBolletjes)
        if hoorntjeOfBakjeStr == "opnieuw":
            opnieuw = True
    nogEenKeer = meerIjsjes(hoorntjeOfBakjeStr, aantalBolletjes)


bon(ijsjesdict)
print("Bedankt en tot ziens!")
