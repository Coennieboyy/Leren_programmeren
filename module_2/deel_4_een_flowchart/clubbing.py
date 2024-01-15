PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

stempel = False
bandje = None

def stelvraag(vraag, antwoorden):
    while True:
        UserInput = input(vraag).lower()
        if UserInput in antwoorden:
            return UserInput
        else:
            print(f"{UserInput} is geen geldig antwoord.\n")


vraag = "hoe oud ben je? "
antwoorden = [str(i) for i in range(1,120)]
leeftijd = int(stelvraag(vraag, antwoorden))

if leeftijd < 18:
    print("sorry je mag niet naar binnen")
    print(f"probeer het in {18 - leeftijd} jaar nog een keer ")

elif leeftijd >= 18:
    vraag = "wat is je naam? "
    antwoorden = input(vraag).lower()

    if antwoorden in VIP_LIST:
        if leeftijd >= 21:
            bandje = "blauw"
        else:
            bandje = "rood"
        print(f"je krijgt van mij een {bandje} bandje")
    else:
        if leeftijd >= 21:
            print("je krijgt van mij een stempel")
            stempel = True
    
    vraag = "wat wil je drinken? "
    antwoorden = input(vraag).lower()

    if antwoorden == "cola":
        prijs = PRIJS_COLA
    elif antwoorden == "bier":
        prijs = PRIJS_BIER
    elif antwoorden == "champagne":
        prijs = PRIJS_CHAMPAGNE
    

    if antwoorden not in DRANKJES:
        print("sorry geen idee wat je bedoeld, hier een glaasje water")
    else:
        gratis = "alstublieft, complimenten van het huis"
        betalen = f"alsjeblieft je {antwoorden}, dat is dan €{prijs}"
        sorry = "sorry je mag geen alcohol bestellen onder de 21"
        tejong = f"probeer het in {21 - leeftijd} jaar nog een keer"

    if antwoorden == "cola" and (bandje == "blauw" or bandje == "rood"):
        print(gratis)
    elif antwoorden == "cola" and bandje == None:
        print(betalen)

    if antwoorden == "bier" and stempel == False and (bandje == "blauw" or bandje == "rood"):
        print(gratis)
    elif antwoorden == "bier" and stempel == True and bandje == None:
        print(betalen)
    elif antwoorden == "bier" and stempel == False and bandje == None:
        print(sorry)
        print(tejong)

    if antwoorden == "champagne" and bandje == "blauw":
        print(betalen)
    elif antwoorden == "champagne" and bandje == "rood":
        print(sorry)
        print(tejong)
    elif antwoorden == "champagne" and bandje == None:
        print("sorry alleen vips mogen champagne bestellen")




