import random

def intantwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = int(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul een integer in")

def verkeerd_getal(raadgetal):
    if raadgetal > 1000 or raadgetal < 1:
        raise ValueError
    
def VraagNieuweRonde(rondes):
    if rondes < 20:
        vakerspelen = input("wil je nog een keer spelen? ").lower()
        if vakerspelen == "nee" or vakerspelen == "n":
            return False
        return True
    return False

randomgetal = random.randint(1,1000)
score = 0
rondes = 1
raden = 0

while True:
    #Vraag om een getal
    try:
        raadgetal = intantwoord("raad een getal tussen 1 en 1000 ")
        verkeerd_getal(raadgetal)
    except ValueError:
        print(f"vul een getal in tussen 1 en 1000!")

    #Rekent het verschil uit    
    verschil = abs(raadgetal-randomgetal)
    HogerOfLager = ""

    #Als het getal het goede getal is
    if raadgetal == randomgetal:
        print(f"goed geraden het getal was {randomgetal}")
        score += 1
        raden = 0
        Doorgaan = VraagNieuweRonde(rondes)
        if Doorgaan == True:
            randomgetal = random.randint(1,1000)
            rondes += 1
            print(f"\nronde {rondes} en score van {score} \n")
            HogerOfLager = "Geraden"
        else:
            break

    #Uitrekenen of het hoger of lager moet zijn en kijken voor hoe warm die is
    if HogerOfLager != "Geraden":
        if raadgetal > randomgetal:
            HogerOfLager = "lager" 
        elif raadgetal < randomgetal:
            HogerOfLager = "hoger"

        if verschil <= 50:
            if verschil <= 20:
                print("Je bent heel warm")
            else:
                print("Je bent warm")
        print(HogerOfLager)

    #Als je het getal niet hebt geraden
    if raadgetal != randomgetal:
        raden += 1
        if raden >= 10:
            print(f"Jammer het getal was {randomgetal}")
            Doorgaan = VraagNieuweRonde(rondes)
            raden = 0
            if Doorgaan == True:
                randomgetal = random.randint(1,1000)
                rondes += 1
                print(f"\nronde {rondes} en score van {score} \n")
            else:
                break
        print(randomgetal)
print(f'''
bedankt voor het spelen 
Je hebt {rondes}x gespeeld
en je hebt een score van {score} behaald.
''')