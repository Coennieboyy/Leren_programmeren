import time,math
from termcolor import colored
from data import *
##################### O03 #####################

def copper2silver(amount:int) -> float: # Functie die koper naar zilver zet
    return round(amount/10,2)

def silver2gold(amount:int) -> float: # Functie die zilver naar goud zet
    return round(amount/5,2)

def copper2gold(amount:int) -> float: # Functie die koper naar goud zet
    return round(amount/50,2)

def platinum2gold(amount:int) -> float: # Functie die platinum naar goud zet
    return round(amount*25,2)

def getPersonCashInGold(personCash:dict) -> float: # Functie zet al het personCash om in goud
    aantalgoud = 0
    if "copper" in personCash:
        aantalgoud += copper2gold(personCash["copper"])
    if "silver" in personCash:
        aantalgoud += silver2gold(personCash["silver"])
    if "platinum" in personCash:
        aantalgoud += platinum2gold(personCash["platinum"])
    if "gold" in personCash:
        aantalgoud += personCash["gold"]

    return round(aantalgoud,2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float: # Functie die de voedsel kosten berekenen van de hele journey
    berekening = copper2gold((people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY)*JOURNEY_IN_DAYS)
    return berekening

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list: # Functie gaat kijken of de value overeen komt met de value van de parameter
    nieuwelist = []
    for info in list:
        if key in info:
            if info[key] == value:
                nieuwelist.append(info) # Voegt de info toe aan een nieuwe lijst(info is de informatie die die krijgt uit de lijst)
    return nieuwelist
                

def getAdventuringPeople(people:list) -> list: # Functie gaat hier de AdventuringPeople verzamelen met behulp van bepaalde value's
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list: # Functie gaat hier de ShareWithFriends verzamelen met behulp van bepaalde value's
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list: # Functie gaat hier de AdventuringFriends verzamelen met behulp van bepaalde value's
    gaanmee = getShareWithFriends(friends)
    return getFromListByKeyIs(gaanmee, 'adventuring', True)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int: # Functie gaat uitrekenen hoeveel paarden er nodig zijn
    #horses = 0

    # for persons in range(people):
    #     horses += 0.5
    # return math.ceil(horses)

    if people % 2 == 0:
        return int(people / 2)
    else:
        return int(people / 2)+1 # else voegt een paard toe

def getNumberOfTentsNeeded(people:int) -> int: # Functie gaat uitrekenen hoeveel tenten er nodig zijn
    # tents = 0

    # for persons in range(people):
    #     tents += 0.33
    # return math.ceil(tents)

    if people % 3 == 0:
        return int(people / 3)
    else:
        return int(people / 3)+1 # else voegt een tent toe

def getTotalRentalCost(horses:int, tents:int) -> float: # Functie gaat berekenen hoeveel de paarden en tenten kosten
    horses_berekening = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    horses_berekening = silver2gold(horses_berekening)
    if JOURNEY_IN_DAYS % 7 == 0:
        tents_berekening = tents * COST_TENT_GOLD_PER_WEEK
    else:
        tents_berekening = tents * (COST_TENT_GOLD_PER_WEEK * 2) # * 2 omdat het langer dan een week is

    return horses_berekening + tents_berekening

##################### O08 #####################

def getItemsAsText(items:list) -> str: # Functie verzameld info door de parameter items
    length = len(items)
    resultaat = ""
    loop = 0
    for item in items:
        resultaat = resultaat + f"{item['amount']}{item['unit']} {item['name']}"
        if length > 1:
            if loop == length-2: # als dit het laatste stuk resultaat is moet er een & teken tussen
                resultaat = resultaat + " & "
            elif loop != length-1:# als dit niet het laatste stuk resultaat is moet er een , teken tussen
                resultaat = resultaat + ", "
            loop += 1   
        
    return resultaat

def getItemsValueInGold(items:list) -> float: # Functie berekend de waarde van de items
    waarde = 0 # Alles wordt toegevoegt aan waarde zodat het allemaal bij elkaar is opgeteld
    for item in items:
        if (item['price']['type'] == 'copper'):
            waarde = waarde + copper2gold(item['price']['amount'])* item['amount']
        if (item['price']['type'] == 'silver'):
            waarde = waarde + silver2gold(item['price']['amount'])* item['amount']
        if (item['price']['type'] == 'platinum'):
            waarde = waarde + platinum2gold(item['price']['amount'])* item['amount']
        if (item['price']['type'] == 'gold'):
            waarde = waarde + item['price']['amount']* item['amount']
    return float(waarde)    
            

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float: # Functie berekend hoeveel goud de parameter people heeft
    geld = 0 # Alles wordt toegevoegt aan geld zodat het allemaal bij elkaar is opgeteld
    for person in people:
        if person['cash']['platinum']:
            geld = geld + platinum2gold(person['cash']['platinum'])
        if person['cash']['gold']:
            geld = geld + (person['cash']['gold'])
        if person['cash']['silver']:
            geld = geld + silver2gold(person['cash']['silver'])
        if person['cash']['copper']:
            geld = geld + copper2gold(person['cash']['copper'])
    return float(geld)
##################### O10 #####################

def getInterestingInvestors(investors:list) -> list: # Functie verzameld investors op basis van de profitreturn onder of gelijk aan 10 omdat het niet meer mag zijn
    investorlist = []
    for invest in investors:
        if invest['profitReturn'] <= 10:
            investorlist.append(invest)
    return investorlist

def getAdventuringInvestors(investors:list) -> list: # Functie verzameld investors op basis van de profitreturn en dat adventuring True moet zijn
    investorlist = []
    for invest in investors:
        if invest['profitReturn'] <= 10 and invest['adventuring'] == True:
            investorlist.append(invest)
    return investorlist

def getTotalInvestorsCosts(investors:list, gear:list) -> float: # berekend hoeveel de investors die meegaan kosten
    investerscount = len(getAdventuringInvestors(investors))
    food = getJourneyFoodCostsInGold(investerscount, investerscount)
    rent = getTotalRentalCost(investerscount, investerscount)
    gear = getItemsValueInGold(gear)
    return float(food + rent + (investerscount * gear)) # berkend alle benodigdheden voor de investors

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int: # Functie berekend hoeveel nachten de mensen en paarden in de inn kunnen blijven
    peoplecost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people 
    horsescost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    Berekening = leftoverGold // (peoplecost + horsescost)
    return int(Berekening)
    

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float: # Functie berekend hoeveel de inn gaat kosten op basis van hoelang en hoeveel mensen er blijven
    peoplecost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horsescost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    Berekening = nightsInInn * (peoplecost + horsescost)
    return round(Berekening,2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list: # Berekend wat de investors krijgen van de journey
    investorcut = []
    interestedinvesters = getInterestingInvestors(investors)
    for investor in interestedinvesters:
        berekening =  round(profitGold * (investor['profitReturn']/100),2) # Berekend hoeveel ze krijgen en rekent het procenten getal om naar komma getal
        investorcut.append(berekening)
    return investorcut

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float: # Berekend hoeveel de adventurer krijgt van de journey
    investorcut = sum(investorsCuts)
    if profitGold != 0: # If statements zodat hij niet kan delen door 0
        profitGold = profitGold - investorcut
    if fellowship != 0:
        sharedGold = profitGold / fellowship
    if fellowship == 0: # If statement voor als de fellowship 0 is
        sharedGold = profitGold * fellowship

    
    return round(sharedGold,2)


##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = []
    interestingInvestors = []
    adventuringInvestors = []
    investorsCuts = []
    goldCut = 0.0

    adventuringFriends.append(getAdventuringFriends(friends))
    interestingInvestors.append(getInterestingInvestors(investors))
    adventuringInvestors.append(getAdventuringInvestors(investors))
    investorsCuts.append(getInvestorsCuts(profitGold))

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen

        earnings.append({
            'name'   : '??',
            'start'  : 0.0,
            'end'    : 0.0
        })

    return earnings

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()