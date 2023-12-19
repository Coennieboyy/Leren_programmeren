bgngetal = 50
totaal = 0
lijst = []


while totaal < 1000:
    totaal += bgngetal
    lijst.append(bgngetal)
    txt = ""
    for getal in lijst:
        txt = txt + str(getal) + " "
        if getal != bgngetal:
            txt = txt + "+ "
    txt = txt + "= " + str(totaal)
    
    bgngetal +=1
    print(txt)