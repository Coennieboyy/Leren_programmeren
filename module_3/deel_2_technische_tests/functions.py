import time,math
from termcolor import colored
from data import *
##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount/10,2)

def silver2gold(amount:int) -> float:
    return round(amount/5,2)

def copper2gold(amount:int) -> float:
    return round(amount/50,2)

def platinum2gold(amount:int) -> float:
    return round(amount*25,2)

def getPersonCashInGold(personCash:dict) -> float:
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

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    berekening = copper2gold((people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY)*JOURNEY_IN_DAYS)
    return berekening

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    nieuwelist = []
    for info in list:
        if key in info:
            if info[key] == value:
                nieuwelist.append(info)
    return nieuwelist
                

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    gaanmee = getShareWithFriends(friends)
    return getFromListByKeyIs(gaanmee, 'adventuring', True)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    #horses = 0

    # for persons in range(people):
    #     horses += 0.5
    # return math.ceil(horses)

    if people % 2 == 0:
        return int(people / 2)
    else:
        return int(people / 2)+1

def getNumberOfTentsNeeded(people:int) -> int:
    # tents = 0

    # for persons in range(people):
    #     tents += 0.33
    # return math.ceil(tents)

    if people % 3 == 0:
        return int(people / 3)
    else:
        return int(people / 3)+1

def getTotalRentalCost(horses:int, tents:int) -> float:
    horses_berekening = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    horses_berekening = silver2gold(horses_berekening)
    if JOURNEY_IN_DAYS % 7 == 0:
        tents_berekening = tents * COST_TENT_GOLD_PER_WEEK
    else:
        tents_berekening = tents * (COST_TENT_GOLD_PER_WEEK * 2)

    return horses_berekening + tents_berekening

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    length = len(items)
    resultaat = ""
    loop = 0
    for item in items:
        resultaat = resultaat + f"{item['amount']}{item['unit']} {item['name']}"
        if length > 1:
            if loop == length-2:   
                resultaat = resultaat + " & "
            elif loop != length-1:
                resultaat = resultaat + ", "
            loop += 1   
        
    return resultaat

def getItemsValueInGold(items:list) -> float:
    waarde = 0
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

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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