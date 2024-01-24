from fruitmand import fruitmand
list = [ ]

for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.remove(fruit)

for fruit in fruitmand:
    if fruit["color"] not in list:
        list.append(fruit["color"])
print(list)
