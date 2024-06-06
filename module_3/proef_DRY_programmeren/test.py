ijsjesdict = {"bakje": {"hoeveelheid":14, "prijs": 1.10},
              "hoorntje": {"hoeveelheid":3, "prijs": 1.25},
              "vanile": {"hoeveelheid":20, "prijs": 0.75}}

toppingsDict = {'slagroom': {'hoeveelheid':3, 'prijs': 0.50},
                'sprinkels': {'hoeveelheid':0, 'prijs': 0.30},
                'caramelSaus': {'hoeveelheid':2, 'prijs': 0.60}}

max = 10
maxtotaal = 20

for ijsje in ijsjesdict:
       print(f"{ijsje}{(max-len(ijsje)) * ' '}{ijsjesdict[ijsje]['hoeveelheid']} x {ijsjesdict[ijsje]['prijs']} = ")

def prijsBerekening(hoeveelheid:int, prijs:float) -> float:
    berekening = hoeveelheid * prijs
    return berekening

for topping in range(len(toppingsDict)):
     toppingsDict[topping]['hoeveelheid'] + toppingsDict[topping]['hoeveelheid'] 

print(len(toppingsDict))