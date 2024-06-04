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
            print(f"{vraag} Sorry, dat snap ik niet")

def antwoord(a:str)-> str:
    while True:
        string = input(a).lower()
        if str.isalpha(string) == True:
            return string
        else:
            print(f"{string} is geen geldig antwoord, vul tekst in")

#------ijsSalon specefiek functies------#

def hoeveelIjs() -> int:
    while True:
        aantal = antwoordint("\nhoeveel bolletjes wilt u? ")
        if aantal > 0:
            ijsjesdict["vanille"]["hoeveelheid"] += aantal
            return aantal
        else:
            print("Voer alstublieft een geldig aantal bolletjes in.")
    
def meerIjsjes(hoorntjeOfBakje:str, aantal:int) -> bool:
    print(f"Hier is uw {hoorntjeOfBakje} met {aantal} bolletje(s)")

    while True:
        meerIjsjesvraag = antwoord("wilt u nog een ijsje? ")
        if meerIjsjesvraag in antwoordlistJa:
            return True
        elif meerIjsjesvraag in antwoordlistNee:
            return False
        else:
            print("Sorry, dat snap ik niet")

def hoorntjeOfbakjeFunctie(aantal:int) -> str:
    while True:
        if aantal in range(1,4):
            hoorntjeBakje = antwoord(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
            if hoorntjeBakje == "bakje":
                ijsjesdict["bakje"]["hoeveelheid"] += 1
                return hoorntjeBakje
            elif hoorntjeBakje == "hoorntje":
                ijsjesdict["hoorntje"]["hoeveelheid"] += 1 
                return hoorntjeBakje
            else:
                print("Sorry, dat snap ik niet")
        elif aantal in range(4,9):
            ijsjesdict["bakje"]["hoeveelheid"] += 1
            return "bakje"
        else:
            print("Sorry, zulke grote bakken hebben we niet")
            return "opnieuw"
        
        


def prijsBerekening(hoeveelheid:int, prijs:float) -> float:
    berekening = hoeveelheid * prijs
    return berekening

def bon(ijsjesdict:dict) -> str:
    print(f"---------[Papi Gelato]---------")
    totaal = 0
    for ijsje in ijsjesdict:
        if ijsjesdict[ijsje]['hoeveelheid'] !=0:
            print(f"{ijsje}{(max-len(ijsje)) * ' '}{ijsjesdict[ijsje]['hoeveelheid']} x {ijsjesdict[ijsje]['prijs']} = {prijsBerekening(ijsjesdict[ijsje]['hoeveelheid'],ijsjesdict[ijsje]['prijs'])}")
            totaal = totaal + prijsBerekening(ijsjesdict[ijsje]['hoeveelheid'],ijsjesdict[ijsje]['prijs'])
            afgerondTotaal = round(totaal,2)
    print("                --------- +")
    print(f"totaal             = {afgerondTotaal}")
