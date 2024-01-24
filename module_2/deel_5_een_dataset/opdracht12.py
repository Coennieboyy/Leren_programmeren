from fruitmand import fruitmand

langstewoord = " "
kleur_fruit = " "
gewicht_fruit = " "

vertaling = {
    "red"    : "rood",
    "orange" : "oranje",
    "yellow" : "geel",
    "green"  : "groen",
    "brown"  : "bruin",
    "purple" : "paars",
    "pink"   : "roze",
    "black"  : "zwart"
    }

for fruit in fruitmand:
    if len(fruit['name']) > len(langstewoord):
        langstewoord = fruit['name']
        kleur_fruit = fruit['color']
        gewicht_fruit = fruit['weight']/1000

zin = print(f"de {langstewoord} ({len(langstewoord)} letters) heeft een {vertaling.get(kleur_fruit)} kleur en een gewicht van {gewicht_fruit}kg")