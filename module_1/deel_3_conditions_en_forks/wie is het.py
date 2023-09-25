userinput = input("is de kaas geel? J/N ")
jalist = ("J" , "j" , "ja" , "JA")
neelist = ("N" , "n" , "nee" , "NEE") 

if userinput in jalist:
    userinput = input("zitten er gaten in? J/N ")
    if userinput in jalist:
        userinput = input("is de kaas belachelijk duur? J/N ")
        if userinput in jalist:
            print("emmenthaler")
        else:
            print("leerdammer")
    elif userinput in neelist:
        userinput = input("is de kaas hard als steen? J/N ")
        if userinput in jalist:
            print("parmigiano reggiano")
        else:
            print("goudse kaas")

elif userinput in neelist:
    userinput = input("heeft de kaas blauwe schimmel? J/N ")
    if userinput in jalist:
        userinput = input("heeft de kaas korst? J/N ")
        if userinput in jalist:
            print("blue de roch baron")
        else:
            print("foume d'ambert")
    else:
        userinput = input("heeft de kaas korst? J/N ")
        if userinput in jalist:
            print("camembert")
        else:
            print("mozzarella")

