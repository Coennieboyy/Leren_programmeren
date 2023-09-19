persoon = 4
toegangsticket =   7.45
gameseat = 0.37 #voor 5 minuten
som = (toegangsticket + (gameseat * 9)) * persoon
antwoord = round(som, 2)

print((f"dit geweldige dagje-uit met 4 mensen in de speelhal met 45 minuten VR kost je maar {antwoord} euro ")) 
