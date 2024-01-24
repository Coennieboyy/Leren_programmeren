from fruitmand import fruitmand


fruitmand.append({"name": "watermeloen",
                  "weight": 3000,
                  "color": "green",
                  "round": True})

for fruit in fruitmand:   
    print(fruit["weight"])