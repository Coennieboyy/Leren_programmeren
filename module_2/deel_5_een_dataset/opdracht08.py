from fruitmand import fruitmand

for fruit in fruitmand:
    fruit.update({"name": "watermeloen",
                  "weight": 3000,
                  "color": "green",
                  "round": True})
    
    print(fruit["weight"])