from random import randint
from functions import *
antwoordlist = [1, 2]
antwoordlistfight = [1, 2, 3]
keuze1 = True
gevecht = False
battle = False
clear_terminal()
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

slow_print("""
"Hey, moet je eens kijken Melodius!"
""")
clear_terminal()

slow_print("""
Je opent je ogen en staat op en ziet 2 mensen vreemd naar je kijken
""")
clear_terminal()

slow_print("""
Heel verward kijk je om je heen
""")
clear_terminal()

(slow_print("""
Je ziet een paar mensen op je afkomen, wat doe je?
1. Je probeert langs hun te komen
2. Je checkt je inventory"""))
afkomen = 0
combat = 0
while keuze1:
    try:
        antwoord1 = ask_for_input("")
        if antwoord1 == 1:
             slow_print("Je probeert langs hun te komen")
             clear_terminal()
             slow_print("Eentje zag dat je langs hun probeerde te komen en greep je vast")
             gevecht = True
             keuze1 = False
             afkomen += 1
        elif antwoord1 == 2:
             slow_print("Je checkt je inventory")
             clear_terminal()
             slow_print("...")
             clear_terminal()
             slow_print("Je vond een gitaarzwaard!")
             slow_print('''Wat ga je doen met de gitaarzwaard?
1. Aanvallen
2. Afwachten''')
             banditen = int(input())
             if banditen == 1:
                  clear_terminal()
                  combat += 1
                  keuze1 = False
                  gevecht = True
             elif banditen == 2:
                  clear_terminal()
                  slow_print('''Het blijkt een paar banditen te zijn, je twijfelt nu wat je wilt
1. Je valt hun als eerst aan
2. Je laat zien dat je een wapen hebt''')
                  banditen2 = ask_for_input("")
                  if banditen2 == 1:
                       clear_terminal()
                       combat += 1
                       keuze1 = False
                       gevecht = True
                  elif banditen2 == 2:
                       clear_terminal()
                       slow_print("Ze zagen je wapen en liepen verder")
                       clear_terminal()
                       slow_print("Je liep verder en vond een dorp waar je terecht kon komen")
                       clear_terminal()
                       slow_print("Je liep verder en kwam een dorp tegen")
                       clear_terminal()
                       slow_print("Iemand kwam op je aflopen")
                       clear_terminal()
                       slow_print("...")
                       slow_print('"HEY"')
                       clear_terminal()
                       slow_print('"Wat zijn je intenties hier jonge man?"')
                       clear_terminal()
                       slow_print('''Zo te zien is het een bewaker van het dorp  
Wat ga je zeggen?
1. "Ik zoek een plek om te wonen en het dorpje hier leek mij een mooie plek"
2. "Ik zou graag willen handelen in uw dorp"''')
                       bewaker = ask_for_input("")
                       if bewaker == 1 and combat == 0:
                        clear_terminal()
                        slow_print("De bewaker vond het een goede reden om je door te laten gaan")
                        clear_terminal()
                        ending("win")

                       keuze1 = False
        elif antwoord1 == 22446688:
                  slow_print("...")
                  slow_print("Wat?")
                  clear_terminal()
                  slow_print('''Je valt op eens flauw en word wakker in een bed
1. Ik wil opstaan en kijken wat er buiten te zien is
2. Ga weer slapen''')
                  secret1 = ask_for_input("")
                  if secret1 == 1:
                       slow_print('''Je weet totaal niet wat er gaande was en liep naar buiten''')
                       clear_terminal()
                       slow_print('En op eens uit het niets moest je hoesten door de lucht en sterfde er uiteindelijk')
                       clear_terminal()
                       ending("died")
                    
                       keuze1 = False
                  elif secret1 == 2:
                       slow_print("...")
                       clear_terminal()
                       slow_print("...")
                       clear_terminal()
                       slow_print("...")
                       slow_print("*Gaap*")
                       clear_terminal()
                       slow_print('''De zon schijnt heerlijk in je gezicht
Je realiseert dat het allemaal een droom was en je ging naar werk''')
                       clear_terminal()
                       ending("win")

                       keuze1 = False             
    except keuze1 is not True:
         print("""ERROR: LOOP WERKT NIET CORRECT""")
while gevecht:
    slow_print('''Je zit nu in een gevecht, wat ga je doen?
1. ATTACK
2. COMMUNICEREN
3. WEGRENNEN
''')
    answer = ask_for_input_fight("")
    if antwoord1 == 2 and answer == 1 and combat == 1:
         clear_terminal()
         slow_print("Je steekt er eentje neer met je gitaarzwaard")
         slow_print("De andere bandiet zag dat je zijn vriend had neergestoken en rende snel weg")
         clear_terminal()
         slow_print("Je liep verder en kwam een dorp tegen")
         clear_terminal()
         slow_print("Iemand kwam op je aflopen")
         clear_terminal
         slow_print("...")
         slow_print('"HEY"')
         clear_terminal()
         slow_print('"Wat zijn je intenties hier jonge man?"')
         clear_terminal()
         slow_print('''Zo te zien is het een bewaker van het dorp  
Wat ga je zeggen?
1. "Ik zoek een plek om te wonen en het dorpje hier leek mij een mooie plek"
2. "Ik zou graag willen handelen in uw dorp"''')
         bewaker = ask_for_input("")
         if bewaker == 1 and combat == 0:
              clear_terminal()
              slow_print("De bewaker vond het een goede reden om je door te laten gaan")
              clear_terminal()
              ending("win")


              gevecht = False
         elif bewaker == 1 and combat == 1:
              clear_terminal()
              slow_print("De bewaker vond het een goeie reden om je door te laten gaan")
              slow_print("...")
              slow_print("Wacht..IS DAT BLOED?")
              clear_terminal()
              slow_print('''Je hart begint hard te kloppen..."Wat moet ik zeggen!?"
1. "Ik werd aangevallen door een paar banditen dus ik verdidigde mezelf"
2. "Ik heb een paar dieven vermoord"
3. Steek de bewaker''')
              bloed = ask_for_input_bewaker("")
              if bloed == 1:
                   clear_terminal()
                   slow_print('"Aah oke, dat betekend dat jij jezelf goed kan verdedigen zie ik. Je bent meer dan welkom!"')
                   clear_terminal()
                   ending("win")


                   gevecht = False
              elif bloed == 2:
                   clear_terminal()
                   slow_print("De bewaker schrok zich en nam je mee naar een gevangenis")
                   clear_terminal()
                   ending("failed")

                   gevecht = False
              elif bloed == 3 and combat == 1:
                   clear_terminal()
                   slow_print("Je was op het moment om weg te lopen maar een paar andere bewakers liepen langs en haalde back-up")
                   clear_terminal()
                   gevecht = False
                   battle = True
         elif bewaker == 2:
              clear_terminal()
              slow_print("De bewaker vond het heel verdacht en schoot je neer")
              clear_terminal()
              ending("died")

              gevecht = False
    elif afkomen == 1 and answer == 1:
          clear_terminal()
          slow_print("Je raakt eentje met je vuisten, maar je realiseert dat je te slap bent")
          clear_terminal()
          ending("died")

          gevecht = False
    elif answer == 3:
          slow_print('''Je probeerde weg te rennen maar 
een van de banditen gooit een sfeerspeer op je''')
          ending("died")


          gevecht = False
    elif answer == 2:
          slow_print("Je probeerde te communiceren")
          slow_print("Maar de banditen hadden geen zin om te praten en staken je neer")
          clear_terminal()
          ending("died")

          gevecht = False

while battle:
     try:
          slow_print('''Je bent op het punt om een groot gevecht te houden met kans dat je bij elke keuze verliest''')
          clear_terminal()
          slow_print('''Bewaker 1 komt op je af
Je herinnert een attack die je hiervoor niet kon doen
                             
1. Gebruik de gitaarzwaard
2. Gebruik een spreuk op de bewaker''')
          inbattle = ask_for_input("")
          if inbattle == 1:
               gokken = randint(1, 2)
               if gokken == 1:
                    slow_print("Je sloeg de eerste bewaker neer maar de andere bewakers bemoeide met het gevecht en je ging dood")
               elif gokken == 2:
                    slow_print("Je sloeg mis en werd vermoord")
               clear_terminal()
          elif inbattle == 2:
               slow_print("Je nam de keuze om een spreuk te gebruiken maar je weet nog niet helemaal hoe het werkt")
               clear_terminal()
               gokken = randint(1, 2)
               if gokken == 1:
                    slow_print("...")
                    slow_print("Je gebruikt een grote spreuk!")
                    slow_print("Het bleek een spreuk te zijn dat iedereen in het dorp weg heb getoverd")
                    slow_print("Dat betekend dat je een heel dorp heb voor jezelf")
                    clear_terminal()
                    ending("win")

                    battle = False
               elif gokken == 2:
                    slow_print("...")
                    slow_print("Je gebruikt een zwakke spreuk")
                    slow_print("De spreuk was zo zwak dat jij je eigen hart op stop zet")
                    clear_terminal()
                    ending("died")

                    battle = False
     except combat != 1:
          print("COMBAT IS NIET GEBRUIKT, RESETTING STORY...")
          clear_terminal()
          keuze1 = True
          battle = False