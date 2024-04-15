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

shuffle = random.shuffle(wachtwoordList)

while True:
    if wachtwoordList[11] in hoofdletterList and wachtwoordList[12] in hoofdletterList:
        shuffle = random.shuffle(wachtwoordList)

    if wachtwoordList[23] in kleineletterList:
        shuffle = random.shuffle(wachtwoordList)

    if wachtwoordList[0] in interpunctiesList and wachtwoordList[23] in interpunctiesList:
        shuffle = random.shuffle(wachtwoordList)

    if wachtwoordList[0:4] in cijfersList:
        shuffle = random.shuffle(wachtwoordList)
    else:
        break 
print(wachtwoordList)
