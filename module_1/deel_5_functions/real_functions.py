import math 

def calculate_cilinder_content(nr1, nr2):
    inhoud = (nr2 / 2) * (nr2 / 2) * math.pi * nr1
    afronding = round(inhoud, 1)
    return print(afronding)


nr1 = int(input("wat is de hoogte van je blik in cm? "))
nr2 = int(input("wat is de diameter van je blik in cm? "))

calculate_cilinder_content(nr1, nr2)