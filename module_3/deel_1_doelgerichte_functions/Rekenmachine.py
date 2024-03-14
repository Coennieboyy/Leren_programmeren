from functions import *

juiste_antwoorden_lijsta = ["a", "b", "c", "d", "e", "f", "g", "h"]

while True:
    choice = antwoord("wat wilt u doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen of\n H) getal halveren? ")
    if choice not in juiste_antwoorden_lijsta:
        print("voer 1 van de opties in")
    else:
        break

n1 = antwoordfloat("vul getal1 in? ")
if choice == "a" and choice in juiste_antwoorden_lijsta:
    n2 = antwoordfloat("vul getal2 in? ")
    berekening = addition(n1, n2)
    print(f"{n1} + {n2} = {berekening}")
elif choice == "b" and choice in juiste_antwoorden_lijsta:
    n2 = antwoordfloat("vul getal2 in? ")
    berekening = substraction(n1, n2)
    print(f"{n1} - {n2} = {berekening}")
elif choice == "c" and choice in juiste_antwoorden_lijsta:
    n2 = antwoordfloat("vul getal2 in? ")
    berekening = multiplication(n1, n2)
    print(f"{n1} x {n2} = {berekening}")
elif choice == "d" and choice in juiste_antwoorden_lijsta:
    while True:
        n2 = antwoordfloat("vul getal2 in? ")
        try:
            berekening = division(n1, n2)
            print(f"{n1} : {n2} = {berekening}")
            break
        except ZeroDivisionError:
            print("kan niet delen door 0")
elif choice == "e" and choice in juiste_antwoorden_lijsta:
    n2 = 1
    berekening = addition(n1, n2)
    print(f"{n1} + {n2} = {berekening}")
elif choice == "f" and choice in juiste_antwoorden_lijsta:
    n2 = 1
    berekening = substraction(n1, n2)
    print(f"{n1} - {n2} = {berekening}")
elif choice == "g" and choice in juiste_antwoorden_lijsta:
    n2 = 2
    berekening = multiplication(n1, n2)
    print(f"{n1} x {n2} = {berekening}")
elif choice == "h" and choice in juiste_antwoorden_lijsta:
    n2 = 2
    berekening = division(n1, n2)
    print(f"{n1} : {n2} = {berekening}")

Doorgaan(berekening)

    