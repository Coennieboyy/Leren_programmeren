toegangsticket =   7.45
gameseat = 0.074 #voor 1 minuut

persoon = int(input("met hoeveel personen ben je? "))
inputgameseat = int(input("hoelang wil je spelen? "))

gameseatkosten = gameseat * inputgameseat
som = (toegangsticket + gameseatkosten) * persoon
antwoord = round(som, 2)

print((f"dit geweldige dagje-uit met {persoon} mensen in de speelhal met {inputgameseat} minuten VR kost je maar {antwoord} euro ")) 