inputcroissant = float(input("hoeveel croisanten wil je? "))
inputstokbrood = float(input("hoeveel stokbroden wil je? "))
inputkortingsbonnen = float(input("hoeveel kortingsbonnen heb je? "))

croissant = 0.39
stokbrood = 2.78
kortingsbonnen = 0.50
som = (inputcroissant * croissant) + (inputstokbrood * stokbrood) - (inputkortingsbonnen * kortingsbonnen)
antwoord = round(som, 2)

print(f"de feestlunch kost je bij de bakker {antwoord}  voor de croissantjes en de stokbroden als de kortingsbonnen nog geldig zijn! ")