import sys
import time
import random   

antwoordlista=["ja","j","nee","n"]
antwoordlistb=["a","b"]
antwoordlistc=["a","b","c"]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

def clear_terminal():
    print("\033c", end="")

def StelVraag(Vraag, antwoordlist, Kies):
    while True:
        try:
            delay_print(Vraag)
            antwoord = input().lower()
            if antwoord not in antwoordlist:
                raise ValueError
            else:
                return antwoord
        except ValueError:
            print(Kies)




def Functievraag(nummer):
    if nummer == 1:
        Vraag = "ga je via de steeg? ja/nee "
        antwoordlist = antwoordlista
        Kies = "kies uit ja/nee"
        antwoord = StelVraag(Vraag, antwoordlist, Kies)

        if antwoord == "ja"or antwoord =="j":
            Functievraag(2)

        elif antwoord == "nee" or antwoord == "n":
            Functievraag(5)
            

    elif nummer == 2:
        Vraag = '''je loopt door de steeg heen en komt een zwerver tegen wat doe je?
                            a: je biedt hem wat geld aan.
                            b: je loopt door
                            voer a of b in '''
        antwoordlist = antwoordlistb
        Kies = "kies uit a/b"
        antwoord = StelVraag(Vraag, antwoordlist, Kies)

        if antwoord == "a":
            clear_terminal()
            delay_print('''hij wordt erg boos en agressief omdat je hem als zwerver ziet en steekt je neer
                                                
                        JE HEBT VERLOREN.''')
        elif antwoord == "b":
            clear_terminal()
            Functievraag(3)

    elif nummer == 3:
        vraag = '''je komt aan de andere kant van de steeg uit. Je ziet je huis al maar de brug staat open wat doe je?
                        a: je sprint in het water en probeert naar de overkant te zwemmen?
                        b: je wacht tot  dat de brug weer beneden is
                        c: je gaat naar links om te zoeken voor een plek om om te lopen '''
        antwoordlist = antwoordlistc
        kies = "kies uit a/b/c"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            delay_print('''Het water is veel te koud en je vriest dood
                
                        JE HEBT VERLOREN.''')
        
        elif antwoord == "b":
            clear_terminal()
            delay_print('''Je komt heel thuis aan maar je bent wel telaat en je vader is erg boos op je!
                
                        JE HEBT VERLOREN MAAR JE BENT WEL HEEL THUIS''')
            
        elif antwoord == "c":
            clear_terminal()
            Functievraag(4)
    
    elif nummer == 4:
        vraag = '''Je ziet rechts je huis maar als je loopt kom je niet optijd thuis. Je ziet ook een fiets staan maar de eigenaar staat verderop?
                            a: Je gaat gewoon naar huis
                            b: Je probeert z'n fiets te stelen '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            delay_print(''''je komt heel thuis maar je komt telaat aan. Je vader is erg boos!
                        
                        JE HEBT VERLOREN MAAR JE BENT WEL HEEL THUIS''')
            
        elif antwoord == "b":
            fietskans = random.randint(0, 10)
            time.sleep(1.5)
            clear_terminal()
            if fietskans > 5:
                delay_print('''je hebt succesvol z'n fiets gestolen en komt optijd thuis.
                            
                            GEWONNEN!!!''')
                
            elif fietskans < 5:
                delay_print('''De eigenaar heeft het door, hij belt de politie en je wordt opgepakt.
                            
                            JE HEBT VERLOREN EN ZIT NU IN DE CELL''')
                
    elif nummer == 5:
        vraag = '''je komt een kruispunt tegen ga je links of rechts? 
                a: rechts
                b: links '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            delay_print('''je bent de juiste kant op gegaan en je komt veilig thuis aan.
                                                    
                        GEWONNEN!!!''')
        
        elif antwoord == "b":
            clear_terminal()
            Functievraag(6)

    elif nummer == 6:
        vraag = '''je raakt verdwaald wat doe je?
                a: je probeert de weg terug te vinden.
                b: je loopt door '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            Functievraag(7)

        elif antwoord == "b":
            clear_terminal()
            Functievraag(9)

    elif nummer == 7:
        vraag = '''je vind de terug weg niet maar komt wel een schuur tegen wat nu?
                a: je gaat naar binnen
                b: je gaat niet naar binnen en loopt verder '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            Functievraag(8)
        
        elif antwoord == "b":
            clear_terminal()
            Functievraag(10)
        
    elif nummer == 8:
        vraag = '''binnen zie je een matras liggen.
                a: je gaat slapen.
                b: je gaat weer naar buiten '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            delay_print('''je slaapt in het schuurtje en overleeft de nacht maar bent niet thuis gekomen 
                                                              
                        JE VADER IS ERG BEZORGT OMDAT JE NIET THUIS BENT GEKOMEN, VERLOREN.''')
            
        elif antwoord == "b":
            clear_terminal()
            delay_print('''buiten zie je de zwerver aan komen rennen met een mes hij steekt je neer omdat je in zijn huis was binnen gegaan.
                        
                        JE BENT DOOD GEGAAN, VERLOREN.''')
            
    elif nummer == 9:
        delay_print('''je loopt door en komt toevallig weer bij de bar uit en probeert vanaf daar weer naar huis te gaan.\n\n''')
        delay_print('''klik enter om door te gaan''')
        input().lower()
        Functievraag(1)

    elif nummer == 10:
        vraag = '''je komt 1 van je minder betrouwbare vrienden tegen, hij vertelt je dat je de andere kant op moet gaan om thuis te komen. Vertrouw je hem?
                a: je vertrouwd hem en gaat de andere kant op.
                b: je vertrouwd hem niet en gaat niet de andere kant op maar je blijft dezelfde kant op gaan. '''
        antwoordlist = antwoordlistb
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            clear_terminal()
            delay_print('''hij vertelde de waarheid en je komt thuis.
                        
                        GEWONNEN!!!''')
        
        elif antwoord == "b":
            clear_terminal()
            delay_print('''je bent de verkeerde kant op gegaan en kon je huis nooit vinden.
                        
                        JE VADER IS ERG BEZORGT OMDAT JE NIET THUIS BENT GEKOMEN, VERLOREN.''')


clear_terminal()

delay_print('''Welkom bij mijn game. Het is winter en je ging gezellig een avondje uit met je vrienden je hebt goed wat drank op en je voelt je allemaal niet meer zo helder.
Aan de eind van de avond kijk je op je horloge en zie je dat al heel laat is je moet snel thuis komen anders is je vader boos. 
je doel is om optijd thuis zien te komen terwijl je dronken bent en niet meer goed weet waar je heen moet, ook zie je een steegje die waarschijnlijk sneller is...
            


                                                               klik enter om door te gaan ''')
klik = input().lower()
clear_terminal()
Functievraag(1)