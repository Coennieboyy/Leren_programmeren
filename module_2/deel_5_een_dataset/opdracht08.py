from fruitmand import fruitmand

gewicht = 0

fruitmand.append({"name": "watermeloen",
                  "weight": 3000,
                  "color": "green",
                  "round": True})

for fruit in fruitmand:
    gewicht = fruit['weight'] + gewicht

print(f"{gewicht}kg")