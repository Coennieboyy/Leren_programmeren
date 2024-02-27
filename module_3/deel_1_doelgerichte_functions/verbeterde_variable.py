# gaat kijken of je kan delen door 2
def Delen_Door_2(getal:int) -> bool:
    return getal % 2 == 0
# draait de zin om
def Zin_Omdraaier(zin:str) -> str:
    woordlijst = zin.split()
    zinomdraaien = woordlijst[::-1]
    nieuwezin = ' '.join(zinomdraaien)
    return nieuwezin

# telt de letters in de zin of woord
def Letter_Teller(woorden:str) -> int:
    woorden_lijst = set(woorden)
    Hoeveel_letters = len(woorden_lijst)
    return Hoeveel_letters 

# bereked gemiddelde letters per woord
def Gemiddel_De_Letters_Per_Woord(woorden:str) -> float:
    woordenlijst = woorden.split()
    
    totaleletters = 0
    for woord in woordenlijst:
        totaleletters += len(woord)

    gemiddeldelijst = totaleletters / len(woordenlijst)
    return gemiddeldelijst

def Rekentafel_Van_12(som:int, berekening:int=10) -> None:
    for getal in range(1, berekening+1):
        antwoord = getal * som
        print(f'{getal} x {som} = {antwoord}')

print(Rekentafel_Van_12(12))