small = 8.99
medium = 18.00
large = 23.80

inputsmall = int(input("hoeveel small pizza's wil je? "))
inputmedium = int(input("hoeveel medium pizza's wil je? ")) 
inputlarge = int(input("hoeveel large pizza's wil je? "))
antwoord = (inputsmall * small) + (inputmedium * medium) + (inputlarge * large)
totaal = round(antwoord , 2)


print("------------------------------------------")
print()
print(f"{inputsmall} small pizza's:  {inputsmall * small}")
print(f"{inputmedium} medium pizza's: {inputmedium * medium}")
print(f"{inputlarge} large pizza's:  {inputlarge * large}")
print(f"totaal:           {totaal}")
print()
print("------------------------------------------")