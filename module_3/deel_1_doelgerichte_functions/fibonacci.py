from functions import antwoord

input = antwoord("hoeveel getallen wil je? ")

def fibonacci_reeks():
    vorige_getal = 0
    huidige_getal = 1
    print ="0, 1, "

    for i in range(input):
        print = print + f"{vorige_getal + huidige_getal}, "
        tijdelijk_getal = vorige_getal + huidige_getal
        vorige_getal =  huidige_getal
        huidige_getal = tijdelijk_getal
    return print

print(fibonacci_reeks())