print("*******************STUDIEADVIES*******************")
print("Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.")
print("Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds")
print("antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.")
print("het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies.")

aantalweken = int(input("Hoeveel weken ben je al bezig met de opleiding? "))
print("Ik voel stress of blokkades biij het maken van programmeeropdrachten. ")
studentinput0 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
print("Ik stel programmeeropdrachten en -uitdagingen uit.")
studentinput1 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
print("Ik denk dat ik geen talent heb voor de opleiding.")
studentinput2 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
print("Ik vermijd assessments (CJV) en feedback van kritische docenten.")
studentinput3 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
print("Ik vergelijk mezelf met anderen die beter lijken te zien.")
studentinput4 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
if aantalweken > 10:
    print("Ik voel geen interesse in nieuwe programmeertechnieken.")
    studentinput5 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))
    print("Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.")
    studentinput6 = int(input("kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit "))




som = studentinput0 + studentinput1 + studentinput2 + studentinput3 + studentinput4
if aantalweken > 10:
    som = studentinput0 + studentinput1 + studentinput2 + studentinput3 + studentinput4 + studentinput5 +studentinput6

if som <= 2:
    print('''Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
        in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
        op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.''')
elif som <= 3:
    print('''Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
        in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!''')
else:
    print('''Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
        het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!''')
