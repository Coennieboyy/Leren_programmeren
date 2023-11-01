import sys
import time

antwoordlista=["ja","j","nee","n"]
antwoordlistb=["a","b"]
antwoordlistc=["a","b","c"]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0005)

def clear_terminal():
    print("\033c", end="")

clear_terminal()

delay_print('''Welkom bij mijn game. Het is winter en je ging gezellig een avondje uit met je vrienden je hebt goed wat drank op en je voelt je allemaal niet meer zo helder.
Aan de eind van de avond kijk je op je horloge en zie je dta al heel laat is je moet snel thuis komen anders is je vader boos. 
je doel is om optijd thuis zien te komen terwijl je dronken bent en niet meer goed weet waar je heen moet, ook zie je een steegje en dat is waarschijnlijk sneller..
            

                                                               klik enter om door te gaan''')
klik = input().lower()
clear_terminal()

# vraag1=input(delay_print("ga je via de steeg? ja/nee"))
#                         #ja = vraag2
#                         #nee = vraag 4

# vraag2=input(delay_print('''je loopt door de steeg heen en komt een zwerver tegen wat doe je?
#                             optie 1: je biedt hem wat geld aan
#                             optie 2:je loopt door'''))
#                         #optie 1 =  hij wordt erg boos en agressief omdat je hem als zwerver ziet en steekt je neer
#                         #optie 2 = vraag 3

# vraag3=input(delay_print('''je komt aan de andere kant van de steeg uit. je ziet je huis al maar de brug staat open, wat doe je?
#                             optie 1: je springt in het wateren probeert naar de overkant te zwemmen 
#                             optie 2: je wacht tot datde brug weer beneden is maar je komt wel later aan
#                             optie 3: optie 3:je gaat naar links om te zoeken voor een plek om om te lopen'''))
#                         #optie 1 = je bent wat later. Maar wel veilig thuis gekomen
#                         #optie 2 = je raakt onderkoeld en vriest dood
#                         #

# vraag4=input(delay_print('''je komt een kruispunt tegenga je links of rechts?'''))
#                         #links = je bent de juiste kant op gegaan en je komt veilig thuis aan
#                         #rechts = vraag 5

# vraag5=input(delay_print('''je raakt verdwaald wat doe je?
#                             optie 1: je probeert de terug weg te vinden
#                             optie 2: je loopt door'''))
#                         #optie 1 = vraag6
#                         #optie 2 = terug naar start


while True:
    try:
        delay_print("ga je via de steeg? ja/nee ")
        vraag1 = input().lower()
        if vraag1 not in antwoordlista:
            raise ValueError
        break
    except ValueError:
        print("kies uit ja/nee")

if vraag1 == "ja"or vraag1 =="j":
    clear_terminal()
    while True:
        try:
            delay_print('''je loopt door de steeg heen en komt een zwerver tegen wat doe je?
                           a: je biedt hem wat geld aan.
                           b: je loopt door
                           voer a of b in ''')
            vraag2 = input().lower()
            if vraag2 not in antwoordlistb:
                raise ValueError
            break
        except ValueError:
            print("kies uit a/b")


if vraag2 == "a":
    clear_terminal()
    delay_print('''hij wordt erg boos en agressief omdat je hem als zwerver ziet en steekt je neer
                                        
                                            JE HEBT VERLOREN.''')
elif vraag2 == "b":
    clear_terminal()
    while True:
        try:
            delay_print('''je komt aan de andere kant van de steeg uit. Je ziet je huis al maar de brug staat open wat doe je?
                   a: je sprint in het water en probeert naar de overkant te zwemmen?
                   b: je wacht tot  dat de brug weer beneden is
                   c: je gaat naar links om te zoeken voor een plek om om te lopen''')
            vraag3 = input().lower()
            if vraag3 not in antwoordlistc:
                raise ValueError
            break
        except ValueError:
            print("kies uit a/b/c")

if vraag3 == "a":
    clear_terminal
    delay_print('''Het water is veel te koud en je vriest dood
                
                             JE HEBT VERLOREN.''')

elif vraag3 == "b":
    clear_terminal
    delay_print('''Je komt heel thuis aan maar je bent wel telaat en je vader is erg boos op je.
                
                                            JE HEBT VERLOREN MAAR JE BENT WEL HEEL THUIS''')
    
elif vraag3 == "c":
    clear_terminal
    while True:
        try:
            delay_print('''Je ziet rechts je huis maar als je loopt kom je niet optijd thuis. Je ziet ook een fiets staan maar de eigenaar staat verderop?
                           a: Je gaat gewoon naar huis
                           b: Je probeert z'n fiets te stelen''')
            vraag4=input().lower()
            if vraag4 not in antwoordlistb:
                raise ValueError
            break
        except ValueError:
            print("kies uit a/b")
    