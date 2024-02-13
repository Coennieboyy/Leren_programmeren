from fruitmand import fruitmand

list = [ ]
rond = 0
niet_rond = 0

def antwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            for fruit in fruitmand:
                if fruit["color"] not in list:
                    list.append(fruit["color"])
            if vraag in list:
                return vraag
            else:
                raise ValueError
        except ValueError:
            print(f"{vraag} is niet een kleur in de list")
    
vraag = antwoord("welke kleur fruit wil je? ")

for fruit in fruitmand:
    if fruit['color'] == vraag:
        if fruit['round'] == True:
            rond += 1
        elif fruit["round"] == False:
            niet_rond +=1
        
if rond >  niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag}")
elif rond < niet_rond:
    print(f"Er zijn {niet_rond - rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraag}")
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {vraag}")

        
 