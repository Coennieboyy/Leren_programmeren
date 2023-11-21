import random

kleuren = ("harten", "klaveren", "schoppen", "ruiten")
getallen = list(range(2,11))
kaarten = getallen + ["boer", "vrouw", "heer", "aas"]
allekaarten = []

for kleur in kleuren:
    for kaart in kaarten:
        allekaarten.append(kleur + " " + str(kaart))

allekaarten.append("joker")
allekaarten.append("joker")

random.shuffle(allekaarten)

for i in range(7):
    print(f"kaart{i +1}: {allekaarten[1]}")
    allekaarten.pop(1)

print(f"rest van de kaarten{len(allekaarten) ,allekaarten}")

