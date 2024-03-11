def antwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = str(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul text in")

def antwoordint(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = int(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul cijfer in")

def Persoonlijke_gegevens():
    persoon = []

    while True:
        naam = antwoord("Naam? ")
        leeftijd = antwoordint("Leeftijd? ")
        woonplaats = antwoord("woonplaats? ")
        persoon.append({"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats,})

        meernamen = antwoord("Wilt u nog meer namen? ")
        if meernamen == "stop":
            return persoon