def antwoord(a:str)-> str:
    while True:
        string = input(a).lower()
        if str.isalpha(string) == True:
            return string
        else:
            print(f"{string} is geen geldig antwoord, vul tekst in")


def antwoordfloat(a)-> float:
    while True:
        vraag = input(a)
        try:
            vraag = float(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul cijfer in")



# Functie returned lijst met daarin dictionary als item voor elk persoon daarin zitten de keys: naam, leeftijd, woonplaats
def Persoonlijke_gegevens()->list:
    persoon = []

    while True:
        naam = antwoord("Naam? ")
        leeftijd = antwoordfloat("Leeftijd? ")
        woonplaats = antwoord("woonplaats? ")
        persoon.append({"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats,})

        meernamen = antwoord("Wilt u nog meer namen? ")
        if meernamen == "stop":
            return persoon

# functie voor + som      
def addition(n1, n2:float)->float:
    return n1 + n2

# functie voor - som
def substraction(n1, n2:float)->float:
    return n1 - n2

# functie voor x som
def multiplication(n1, n2:float)->float:
    return n1 * n2

# functie voor : som
def division(n1, n2:float) ->float:
    return n1 / n2

# functie voor het doorgaan van de berekening   
def Doorgaan(berekening:float)-> float:
    juiste_antwoorden_lijstb = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    while True:
        choice = antwoord(f"wil je nog iets anders met {berekening} doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen,\n H) getal halveren?,\n I) stoppen ")
        if choice == "a" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = antwoordfloat("vul getal2 in? ")
            berekening = addition(n1, n2)
            print(f"{n1} + {n2} = {berekening}")
        elif choice == "b" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = antwoordfloat("vul getal2 in? ")
            berekening = substraction(n1, n2)
            print(f"{n1} - {n2} = {berekening}")
        elif choice == "c" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = antwoordfloat("vul getal2 in? ")
            berekening = multiplication(n1, n2)
            print(f"{n1} x {n2} = {berekening}")
        elif choice == "d" and choice in juiste_antwoorden_lijstb:
            while True:
                n2 = antwoordfloat("vul getal2 in? ")
                try:
                    berekening = division(n1, n2)
                    print(f"{n1} : {n2} = {berekening}")
                    break
                except ZeroDivisionError:
                    print("kan niet delen door 0")
        elif choice == "e" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = 1
            berekening = addition(n1, n2)
            print(f"{n1} + {n2} = {berekening}")
        elif choice == "f" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = 1
            berekening = substraction(n1, n2)
            print(f"{n1} - {n2} = {berekening}")
        elif choice == "g" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = 2
            berekening = multiplication(n1, n2)
            print(f"{n1} x {n2} = {berekening}")
        elif choice == "h" and choice in juiste_antwoorden_lijstb:
            n1 = berekening
            n2 = 2
            berekening = division(n1, n2)
            print(f"{n1} : {n2} = {berekening}")
        elif choice == "i" and choice in juiste_antwoorden_lijstb:
            eindantwoord = f"dit is je eindantwoord: {berekening}"
            return print(eindantwoord)
        else:
            print("voer 1 van de opties in")