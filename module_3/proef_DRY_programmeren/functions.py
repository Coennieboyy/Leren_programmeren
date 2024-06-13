from data import *

def antwoordfloat(a)-> float:
    while True:
        vraag = input(a)
        try:
            vraag = float(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul cijfer in")

def antwoordint(a)-> int:
    while True:
        vraag = input(a)
        try:
            vraag = int(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} Sorry dat is geen optie die we aanbieden...")

def antwoord(a:str)-> str:
    while True:
        string = input(a).lower()
        if str.isalpha(string) == True:
            return string
        else:
            print(f"{string} is geen geldig antwoord, vul tekst in")

#------ijsSalon specefiek functies------#
def soortKlant():
    while True:
        klant = int(antwoordint("Bent u 1) een particuliere klant of 2) een zakelijke klant? "))
        if klant == 1:
            return True
        elif klant == 2:
            return False
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def hoeveelIjs(KlantBool:bool) -> int:
    while True:
        if KlantBool:
            aantal = antwoordint("\nhoeveel bolletjes wilt u? ")
            if aantal in range(1,9):
                return aantal
            else:
                print("Voer alstublieft een geldig aantal bolletjes in.")
        else:
            aantal = antwoordint("\nhoeveel liters wilt u? ")
        return aantal


def welkeSmaak(aantal:int,ijsjesdict:dict,smaken:dict, klantBool:bool)-> dict:
    if klantBool:
        bOrL = "bolletje"
    else:
        bOrL = "liter"
    for bolletjes in range(aantal):
        while True: 
            soortBol = antwoord(f"Welke smaak wilt u voor {bOrL} nummer {bolletjes + 1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?” ")
            if soortBol in list(smaken.keys()):
                ijsjesdict[smaken[soortBol]]["hoeveelheid"] += 1
                break  
            else:
                print("Sorry dat is geen optie die we aanbieden...")
    return ijsjesdict
    
def meerIjsjes(hoorntjeOfBakje:str, aantal:int) -> bool:
    print(f"Hier is uw {hoorntjeOfBakje} met {aantal} bolletje(s)")

    while True:
        meerIjsjesvraag = antwoord("wilt u nog een ijsje? ")
        if meerIjsjesvraag in antwoordlistJa:
            return True
        elif meerIjsjesvraag in antwoordlistNee:
            return False
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def hoorntjeOfbakjeFunctie(aantal:int) -> str:
    while True:
        if aantal in range(1,4):
            hoorntjeBakje = antwoord(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
            # To do kijken of het slimmer kan.
            if hoorntjeBakje in antwoordlistBakjeOfHoorntje:
                ijsjesdict[hoorntjeBakje]["hoeveelheid"] += 1
                return hoorntjeBakje
            else:
                print("Sorry dat is geen optie die we aanbieden...")
        elif aantal in range(4,9):
            ijsjesdict["bakje"]["hoeveelheid"] += 1
            return "bakje"
        
def topping(hoorntjeBakje:str, aantal:int) -> dict:
    while True:
        soortTopping = antwoord("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if soortTopping in antwoorddictToppings:
            if soortTopping == "a":
                return toppingsDict
            elif soortTopping == "d" and hoorntjeBakje == "bakje":
                toppingsDict["caramelSausB"]["hoeveelheid"] += 1
                return toppingsDict
            elif soortTopping == "c":
                toppingsDict["sprinkels"]["hoeveelheid"] += aantal
                return toppingsDict
            else:
                if soortTopping in list(antwoorddictToppings.keys()):
                    toppingsDict[antwoorddictToppings[soortTopping]]["hoeveelheid"] += 1
                    return toppingsDict
        else:
            print("Sorry dat is geen optie die we aanbieden...")


def prijsBerekening(hoeveelheid:int, prijs:float) -> float:
    berekening = hoeveelheid * prijs
    return round(berekening,2)

def bon(ijsjesdict:dict,klantBool:bool) -> str:
    print(f"---------[Papi Gelato]---------")
    totaal = 0
    toppingtotaal = 0
    toppingCheck = False
    for ijsje in ijsjesdict:
        if ijsjesdict[ijsje]['hoeveelheid'] != 0:
            print(f"{ijsje}{(max-len(ijsje)) * ' '}{ijsjesdict[ijsje]['hoeveelheid']} x {ijsjesdict[ijsje]['prijs']} = {prijsBerekening(ijsjesdict[ijsje]['hoeveelheid'],ijsjesdict[ijsje]['prijs']):.2f}")
            totaal = totaal + prijsBerekening(ijsjesdict[ijsje]['hoeveelheid'],ijsjesdict[ijsje]['prijs'])
            afgerondTotaal = round(totaal,2)

    for topping in toppingsDict:
        if toppingsDict[topping]['hoeveelheid'] != 0:
            toppingCheck = True
            toppingtotaal = toppingtotaal + prijsBerekening(toppingsDict[topping]['hoeveelheid'],toppingsDict[topping]['prijs'])
            afgerondtoppingTotaal = round(toppingtotaal,2)
        else:
            afgerondtoppingTotaal = 0
    if toppingCheck:
        print(f"Toppings{(max-len(topping)) * ' '}              {toppingtotaal:.2f}")
    print("                --------- +")    
    print(f"totaal             = {afgerondTotaal+afgerondtoppingTotaal:.2f}")
    if klantBool == False:
        print(f"BTW (9%)           = {(afgerondTotaal + afgerondtoppingTotaal)/100 * 9:.2f}")