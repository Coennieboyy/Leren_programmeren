def antwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = str(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul text in")

boodschappen = {}

while True:
    item = input("Wat wil je halen? ").lower()
    if item in boodschappen:
        boodschappen[item] += 1
    else:
        boodschappen.update({item : 1})

    meerboodschappen = antwoord("wil je nog meer toevoegen? ")
    if meerboodschappen == "nee" or meerboodschappen == "n":
        print("-[ boodschappenlijst ]- \n")
        for i in boodschappen:
            print(f"{boodschappen[i]} x {i}")
        print("-----------------------")
        break