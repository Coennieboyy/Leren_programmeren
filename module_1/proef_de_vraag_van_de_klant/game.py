import sys
import time




    


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

def clear_terminal():
    print("\033c", end="")

delay_print(f'''Welkom bij mijn game. Je ging gezellig een avondje uit met je vrienden je hebt goed wat drank op en je voelt je allemaal niet meer zo helder.
Aan de eind van de avond beginnen al je vrienden 1 voor 1 naar huis, poosje later gaat ook de laatste we, dus je besluit ook tegaan. 
je doel is om thuis zien te komen terwijl je dronken bent en niet meer goed weet waar je heen moet, ook zie je een steegje en dat is waarschijnlijk sneller..''')
            
klik=input(delay_print('''
                                                               klik enter om door te gaan'''))
clear_terminal()

vraag1=input(delay_print("ga je via de steeg? ja/nee"))
                        #ja = vraag2
                        #nee = vraag 4

vraag2=input(delay_print('''je loopt door de steeg heen en komt een zwerver tegen wat doe je?
                            optie 1: je biedt hem wat geld aan
                            optie 2:je loopt door'''))
                        #optie 1 =  hij wordt erg boos en agressief omdat je hem als zwerver ziet en steekt je neer
                        #optie 2 = vraag 3

vraag3=input(delay_print('''je komt aan de andere kant van de steeg uit. je ziet je huis al maar de brug staat open, wat doe je?
                            optie 1: je springt in het wateren probeert naar de overkant te zwemmen 
                            optie 2: je wacht tot datde brug weer beneden is maar je komt wel later aan'''))
                        #optie 1 = je bent wat later. Maar wel veilig thuis gekomen
                        #optie 2 = je raakt onderkoeld en vriest dood

vraag4=input(delay_print('''je komt een kruispunt tegenga je links of rechts?'''))
                        #links = je bent de juiste kant op gegaan en je komt veilig thuis aan
                        #rechts = vraag 5

vraag5=input(delay_print('''je raakt verdwaald wat doe je?
                            optie 1: je probeert de terug weg te vinden
                            optie 2: je loopt door'''))
                        #optie 1 = vraag6
                        #optie 2 = terug naar start

if vraag1 == "ja":
    delay_print("je komt aan de andere kant van de steeg uit. je ziet je huis al maar de brug staat open, wat doe je?")

    





