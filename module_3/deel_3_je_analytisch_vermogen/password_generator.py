import random

hoofdletterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
kleineletterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cijfersList = ['1','2', '3', '4', '5', '6', '7', '8', '9']
interpunctiesList = ['@', '#', '$', '%', '&', '_', '?']
wachtwoordList = []

for hoofdletters in range(random.randint(2,6)):
    choiceHoofdletters = random.choice(hoofdletterList)
    wachtwoordList.append(choiceHoofdletters)

for interpuncties in range(4):
    choiceInterpuncties = random.choice(interpunctiesList)
    wachtwoordList.append(choiceInterpuncties)

for cijfers in range(random.randint(4,7)):
    choiceCijfers = random.choice(cijfersList)
    wachtwoordList.append(choiceCijfers)

nodigelengte = 24 - len(wachtwoordList)

for kleineletters in range(nodigelengte):
    choiceKleineletters = random.choice(kleineletterList)
    wachtwoordList.append(choiceKleineletters)


while True:
    random.shuffle(wachtwoordList)
    checkTrue1 = False
    checkTrue2 = False
    checkTrue3 = False
    checkTrue4 = False

    if wachtwoordList[11] not in hoofdletterList and wachtwoordList[12] not in hoofdletterList: # if statements om te checken dat sommige opties niet op de verkeerde plek staan
        checkTrue1 = True

    if wachtwoordList[23] not in kleineletterList:
        checkTrue2 = True

    if wachtwoordList[0] not in interpunctiesList and wachtwoordList[23] not in interpunctiesList:
        checkTrue3 = True

    if wachtwoordList[0] not in cijfersList and wachtwoordList[1] not in cijfersList and wachtwoordList[2] not in cijfersList:
        checkTrue4 = True
    
    if checkTrue1 and checkTrue2 and checkTrue3 and checkTrue4: # if statement om te checken dat alle if's True zijn 
        break
    else:
        print(checkTrue1, checkTrue2, checkTrue3, checkTrue4) # else voor debuggen

wachtwoord = "".join(wachtwoordList)
print(f"dit is jou gegenereerdewachtwoord: {wachtwoordList}")

print(wachtwoordList[11]) # prints voor debuggen
print(wachtwoordList[12])
print(wachtwoordList[23])
print(wachtwoordList[0])
print(wachtwoordList[0:3])
