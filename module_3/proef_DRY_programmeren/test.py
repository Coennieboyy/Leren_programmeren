ijsjesdict = {"bakje": {"hoeveelheid":14, "prijs": 1.10},
              "hoorntje": {"hoeveelheid":3, "prijs": 1.25},
              "vanile": {"hoeveelheid":20, "prijs": 0.75}}

max = 10
maxtotaal = 20

for ijsje in ijsjesdict:
       print(f"{ijsje}{(max-len(ijsje)) * ' '}{ijsjesdict[ijsje]['hoeveelheid']} x {ijsjesdict[ijsje]['prijs']} = ")

def prijsBerekening(hoeveelheid:int, prijs:float) -> float:
    berekening = hoeveelheid * prijs
    return berekening