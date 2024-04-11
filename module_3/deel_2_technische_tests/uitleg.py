def dubbel_antwoord(getal1:int, getal2:int) -> int:
    berekenlijst = [] 
    berekenlijst.append(getal1 - getal2)
    berekenlijst.append(getal1 + getal2)
    return berekenlijst




antwoord = dubbel_antwoord(10,20)
print(antwoord)