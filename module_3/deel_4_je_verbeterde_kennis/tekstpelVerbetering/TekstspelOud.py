import sys
import time
import os
from random import randint
antwoordlist = [1, 2]
antwoordlistfight = [1, 2, 3]
def slow_print(text, delay=0.045):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
def slow_print_dot(text, delay=0.5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
def slow_print_verhaal(text, delay=0.035):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def clear_terminal(delay=3):
      time.sleep(delay)
      os.system('cls')
def clear_terminal_verhaal(delay=1):
      time.sleep(delay)
      os.system('cls')
def clear_terminal_error(delay=0.0):
      time.sleep(delay)
      os.system('cls')
def ask_for_input(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 or user_input == 22446688:
                 return user_input
            if user_input != 1 or user_input != 2:
                 raise ValueError
        except ValueError:
            print("Ongeldige invoer. Voer 1 of 2 in.")
def ask_for_input_fight(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 or user_input == 3:
                 return user_input
            if user_input != 1 or user_input != 2 or user_input != 3:
                 raise ValueError
        except ValueError:
            print("Ongeldige invoer. Voer 1, 2 of 3 in.")
def ask_for_input_bewaker(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 and combat == 0 or user_input == 3 and combat == 1:
                 return user_input
            if user_input != 1 or user_input != 2 or user_input != 3:
                 raise ValueError
            if user_input == 3 and combat == 0:
                 slow_print_verhaal("Je durft het niet")
        except ValueError:
            print("Ongeldige invoer. Voer 1 of 2 in.")
keuze1 = True
gevecht = False
battle = False
clear_terminal_error()
print("""
===========================================================
                    Welkom in Harmonia
===========================================================""")
slow_print("""
Je bent een verdwaalde avonturier die zoekt naar een plek
om te wonen.
      
Je bent beland in een bos waar je wakker bent geworden
Geen idee van hoe dit is gebeurd en geen herrinnering van hoe
je hier bent gekomen.
      
Zoek een plek om te kunnen schuilen""")
clear_terminal()

slow_print_verhaal("""
"Hey, moet je eens kijken Melodius!"
""")
clear_terminal_verhaal()

slow_print_verhaal("""
Je opent je ogen en staat op en ziet 2 mensen vreemd naar je kijken
""")
clear_terminal_verhaal()

slow_print_verhaal("""
Heel verward kijk je om je heen
""")
clear_terminal_verhaal()

(slow_print_verhaal("""
Je ziet een paar mensen op je afkomen, wat doe je?
1. Je probeert langs hun te komen
2. Je checkt je inventory"""))
afkomen = 0
combat = 0
while keuze1 == True:
    try:
        antwoord1 = ask_for_input("")
        if antwoord1 == 1:
             slow_print_verhaal("Je probeert langs hun te komen")
             clear_terminal_verhaal()
             slow_print_verhaal("Eentje zag dat je langs hun probeerde te komen en greep je vast")
             gevecht = True
             keuze1 = False
             afkomen += 1
        elif antwoord1 == 2:
             slow_print_verhaal("Je checkt je inventory")
             clear_terminal_verhaal()
             slow_print_dot("...")
             clear_terminal_verhaal()
             slow_print_verhaal("Je vond een gitaarzwaard!")
             slow_print_verhaal('''Wat ga je doen met de gitaarzwaard?
1. Aanvallen
2. Afwachten''')
             banditen = int(input())
             if banditen == 1:
                  clear_terminal_verhaal()
                  combat += 1
                  keuze1 = False
                  gevecht = True
             elif banditen == 2:
                  clear_terminal_error()
                  slow_print_verhaal('''Het blijkt een paar banditen te zijn, je twijfelt nu wat je wilt
1. Je valt hun als eerst aan
2. Je laat zien dat je een wapen hebt''')
                  banditen2 = ask_for_input("")
                  if banditen2 == 1:
                       clear_terminal_verhaal()
                       combat += 1
                       keuze1 = False
                       gevecht = True
                  elif banditen2 == 2:
                       clear_terminal_verhaal()
                       slow_print_verhaal("Ze zagen je wapen en liepen verder")
                       clear_terminal_verhaal()
                       slow_print_verhaal("Je liep verder en vond een dorp waar je terecht kon komen")
                       clear_terminal_verhaal()
                       slow_print_verhaal("Je liep verder en kwam een dorp tegen")
                       clear_terminal_verhaal()
                       slow_print_verhaal("Iemand kwam op je aflopen")
                       clear_terminal_verhaal
                       slow_print_dot("...")
                       slow_print_verhaal('"HEY"')
                       clear_terminal_verhaal()
                       slow_print_verhaal('"Wat zijn je intenties hier jonge man?"')
                       clear_terminal_verhaal()
                       slow_print_verhaal('''Zo te zien is het een bewaker van het dorp  
Wat ga je zeggen?
1. "Ik zoek een plek om te wonen en het dorpje hier leek mij een mooie plek"
2. "Ik zou graag willen handelen in uw dorp"''')
                       bewaker = ask_for_input("")
                       if bewaker == 1 and combat == 0:
                        clear_terminal_verhaal()
                        slow_print_verhaal("De bewaker vond het een goede reden om je door te laten gaan")
                        clear_terminal_verhaal()
                        print('''
 __   __  _______  __   __    _     _  ___   __    _ 
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
|       ||  | |  ||  |_|  |  |       ||   | |       |
|_     _||  |_|  ||       |  |       ||   | |  _    |
  |   |  |       ||       |  |   _   ||   | | | |   |
  |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
                       keuze1 = False
        elif antwoord1 == 22446688:
                  slow_print_dot("...")
                  slow_print_verhaal("Wat?")
                  clear_terminal_verhaal()
                  slow_print_verhaal('''Je valt op eens flauw en word wakker in een bed
1. Ik wil opstaan en kijken wat er buiten te zien is
2. Ga weer slapen''')
                  secret1 = ask_for_input("")
                  if secret1 == 1:
                       slow_print_verhaal('''Je weet totaal niet wat er gaande was en liep naar buiten''')
                       clear_terminal_verhaal()
                       slow_print_verhaal('En op eens uit het niets moest je hoesten door de lucht en sterfde er uiteindelijk')
                       clear_terminal_verhaal()
                       print('''
 __   __  _______  __   __    ______   ___   _______  ______   ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | |      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    ||___   | 
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |  __|  | 
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   | |_____| 
  |   |  |       ||       |  |       ||   | |   |___ |       |   __    
  |___|  |_______||_______|  |______| |___| |_______||______|   |__|''')
                       keuze1 = False
                  elif secret1 == 2:
                       slow_print_dot("...")
                       clear_terminal()
                       slow_print_dot("...")
                       clear_terminal_verhaal()
                       slow_print_dot("...")
                       slow_print("*Gaap*")
                       clear_terminal_verhaal()
                       slow_print_verhaal('''De zon schijnt heerlijk in je gezicht
Je realiseert dat het allemaal een droom was en je ging naar werk''')
                       clear_terminal_verhaal()
                       print('''
 __   __  _______  __   __    _     _  _______  __    _                                                                     
|  | |  ||       ||  | |  |  | | _ | ||       ||  |  | |                                                                    
|  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| |                                                                    
|       ||  | |  ||  |_|  |  |       ||  | |  ||       |                                                                    
|_     _||  |_|  ||       |  |       ||  |_|  ||  _    |                                                                    
  |   |  |       ||       |  |   _   ||       || | |   |                                                                    
  |___|  |_______||_______|  |__| |__||_______||_|  |__|                                                                    
                                                                                                                            
                                                                                                                            
                                                                                                                            
                                                                                                                            
 _____   _______  _______  _______  ______    _______  _______    _______  __    _  ______   ___   __    _  _______  _____  
|     | |       ||       ||       ||    _ |  |       ||       |  |       ||  |  | ||      | |   | |  |  | ||       ||     | 
|    _| |  _____||    ___||       ||   | ||  |    ___||_     _|  |    ___||   |_| ||  _    ||   | |   |_| ||    ___||_    | 
|   |   | |_____ |   |___ |       ||   |_||_ |   |___   |   |    |   |___ |       || | |   ||   | |       ||   | __   |   | 
|   |   |_____  ||    ___||      _||    __  ||    ___|  |   |    |    ___||  _    || |_|   ||   | |  _    ||   ||  |  |   | 
|   |_   _____| ||   |___ |     |_ |   |  | ||   |___   |   |    |   |___ | | |   ||       ||   | | | |   ||   |_| | _|   | 
|_____| |_______||_______||_______||___|  |_||_______|  |___|    |_______||_|  |__||______| |___| |_|  |__||_______||_____|''')
                       keuze1 = False             
    except keuze1 is not True:
         print("""ERROR: LOOP WERKT NIET CORRECT""")
while gevecht == True:
    slow_print('''Je zit nu in een gevecht, wat ga je doen?
1. ATTACK
2. COMMUNICEREN
3. WEGRENNEN
''')
    answer = ask_for_input_fight("")
    if antwoord1 == 2 and answer == 1 and combat == 1:
         clear_terminal_error()
         slow_print_verhaal("Je steekt er eentje neer met je gitaarzwaard")
         slow_print_verhaal("De andere bandiet zag dat je zijn vriend had neergestoken en rende snel weg")
         clear_terminal_verhaal()
         slow_print_verhaal("Je liep verder en kwam een dorp tegen")
         clear_terminal_verhaal()
         slow_print_verhaal("Iemand kwam op je aflopen")
         clear_terminal_verhaal
         slow_print_dot("...")
         slow_print_verhaal('"HEY"')
         clear_terminal_verhaal()
         slow_print_verhaal('"Wat zijn je intenties hier jonge man?"')
         clear_terminal_verhaal()
         slow_print_verhaal('''Zo te zien is het een bewaker van het dorp  
Wat ga je zeggen?
1. "Ik zoek een plek om te wonen en het dorpje hier leek mij een mooie plek"
2. "Ik zou graag willen handelen in uw dorp"''')
         bewaker = ask_for_input("")
         if bewaker == 1 and combat == 0:
              clear_terminal_verhaal()
              slow_print_verhaal("De bewaker vond het een goede reden om je door te laten gaan")
              clear_terminal_verhaal()
              print('''
 __   __  _______  __   __    _     _  ___   __    _ 
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
|       ||  | |  ||  |_|  |  |       ||   | |       |
|_     _||  |_|  ||       |  |       ||   | |  _    |
  |   |  |       ||       |  |   _   ||   | | | |   |
  |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
              gevecht = False
         elif bewaker == 1 and combat == 1:
              clear_terminal_verhaal()
              slow_print_verhaal("De bewaker vond het een goeie reden om je door te laten gaan")
              slow_print_dot("...")
              slow_print_verhaal("Wacht..IS DAT BLOED?")
              clear_terminal_verhaal()
              slow_print_verhaal('''Je hart begint hard te kloppen..."Wat moet ik zeggen!?"
1. "Ik werd aangevallen door een paar banditen dus ik verdidigde mezelf"
2. "Ik heb een paar dieven vermoord"
3. Steek de bewaker''')
              bloed = ask_for_input_bewaker("")
              if bloed == 1:
                   clear_terminal_verhaal()
                   slow_print_verhaal('"Aah oke, dat betekend dat jij jezelf goed kan verdedigen zie ik. Je bent meer dan welkom!"')
                   clear_terminal_verhaal()
                   print('''
 __   __  _______  __   __    _     _  ___   __    _ 
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
|       ||  | |  ||  |_|  |  |       ||   | |       |
|_     _||  |_|  ||       |  |       ||   | |  _    |
  |   |  |       ||       |  |   _   ||   | | | |   |
  |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
                   gevecht = False
              elif bloed == 2:
                   clear_terminal_verhaal()
                   slow_print_verhaal("De bewaker schrok zich en nam je mee naar een gevangenis")
                   clear_terminal_verhaal()
                   print('''
 __   __  _______  __   __    _______  _______  ___   ___      _______  ______  
|  | |  ||       ||  | |  |  |       ||   _   ||   | |   |    |       ||      | 
|  |_|  ||   _   ||  | |  |  |    ___||  |_|  ||   | |   |    |    ___||  _    |
|       ||  | |  ||  |_|  |  |   |___ |       ||   | |   |    |   |___ | | |   |
|_     _||  |_|  ||       |  |    ___||       ||   | |   |___ |    ___|| |_|   |
  |   |  |       ||       |  |   |    |   _   ||   | |       ||   |___ |       |
  |___|  |_______||_______|  |___|    |__| |__||___| |_______||_______||______|''')
                   gevecht = False
              elif bloed == 3 and combat == 1:
                   clear_terminal_verhaal()
                   slow_print_verhaal("Je was op het moment om weg te lopen maar een paar andere bewakers liepen langs en haalde back-up")
                   clear_terminal_verhaal()
                   gevecht = False
                   battle = True
         elif bewaker == 2:
              clear_terminal_verhaal()
              slow_print_verhaal("De bewaker vond het heel verdacht en schoot je neer")
              clear_terminal_verhaal()
              print('''
 __   __  _______  __   __    ______   ___   _______  ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    |
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   |
  |   |  |       ||       |  |       ||   | |   |___ |       |
  |___|  |_______||_______|  |______| |___| |_______||______| ''')
              gevecht = False
    elif afkomen == 1 and answer == 1:
          clear_terminal_error()
          slow_print_verhaal("Je raakt eentje met je vuisten, maar je realiseert dat je te slap bent")
          clear_terminal_verhaal()
          print('''
 __   __  _______  __   __    ______   ___   _______  ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    |
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   |
  |   |  |       ||       |  |       ||   | |   |___ |       |
  |___|  |_______||_______|  |______| |___| |_______||______| ''')
          gevecht = False
    elif answer == 3:
          slow_print_verhaal('''Je probeerde weg te rennen maar 
een van de banditen gooit een sfeerspeer op je''')
          print('''
 __   __  _______  __   __    ______   ___   _______  ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    |
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   |
  |   |  |       ||       |  |       ||   | |   |___ |       |
  |___|  |_______||_______|  |______| |___| |_______||______| ''')
          gevecht = False
    elif answer == 2:
          slow_print_verhaal("Je probeerde te communiceren")
          slow_print_verhaal("Maar de banditen hadden geen zin om te praten en staken je neer")
          clear_terminal_verhaal()
          print('''
 __   __  _______  __   __    ______   ___   _______  ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    |
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   |
  |   |  |       ||       |  |       ||   | |   |___ |       |
  |___|  |_______||_______|  |______| |___| |_______||______| ''')
          gevecht = False

while battle == True:
     try:
          slow_print_verhaal('''Je bent op het punt om een groot gevecht te houden met kans dat je bij elke keuze verliest''')
          clear_terminal()
          slow_print_verhaal('''Bewaker 1 komt op je af
Je herinnert een attack die je hiervoor niet kon doen
                             
1. Gebruik de gitaarzwaard
2. Gebruik een spreuk op de bewaker''')
          inbattle = ask_for_input("")
          if inbattle == 1:
               gokken = randint(1, 2)
               if gokken == 1:
                    slow_print_verhaal("Je sloeg de eerste bewaker neer maar de andere bewakers bemoeide met het gevecht en je ging dood")
               elif gokken == 2:
                    slow_print_verhaal("Je sloeg mis en werd vermoord")
               clear_terminal_verhaal()
          elif inbattle == 2:
               slow_print_verhaal("Je nam de keuze om een spreuk te gebruiken maar je weet nog niet helemaal hoe het werkt")
               clear_terminal_verhaal()
               gokken = randint(1, 2)
               if gokken == 1:
                    slow_print_dot("...")
                    slow_print_verhaal("Je gebruikt een grote spreuk!")
                    slow_print_verhaal("Het bleek een spreuk te zijn dat iedereen in het dorp weg heb getoverd")
                    slow_print_verhaal("Dat betekend dat je een heel dorp heb voor jezelf")
                    clear_terminal_verhaal()
                    print('''
 __   __  _______  __   __    _     _  ___   __    _ 
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
|       ||  | |  ||  |_|  |  |       ||   | |       |
|_     _||  |_|  ||       |  |       ||   | |  _    |
  |   |  |       ||       |  |   _   ||   | | | |   |
  |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
                    battle = False
               elif gokken == 2:
                    slow_print_dot("...")
                    slow_print_verhaal("Je gebruikt een zwakke spreuk")
                    slow_print_verhaal("De spreuk was zo zwak dat jij je eigen hart op stop zet")
                    clear_terminal_verhaal()
                    print('''
 __   __  _______  __   __    ______   ___   _______  ______  
|  | |  ||       ||  | |  |  |      | |   | |       ||      | 
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    |
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   |
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   |
  |   |  |       ||       |  |       ||   | |   |___ |       |
  |___|  |_______||_______|  |______| |___| |_______||______| ''')
                    battle = False
     except combat != 1:
          print("COMBAT IS NIET GEBRUIKT, RESETTING STORY...")
          clear_terminal()
          keuze1 = True
          battle = False
