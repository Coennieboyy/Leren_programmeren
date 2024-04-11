from RobotArm import RobotArm

robotArm = RobotArm('toets-2')

# Je mist twee functies, de moveArm en moveBlock. Dit is de reden dat de robotArm niet goed opstart. 
# Deze functies bevatten beide twee parameters. Jij gaat die functies bouwen. 
# Handig om te weten is dat de functie moveArm ook wordt aangeroepen in de moveBlock functie. 

# De moveBlock functie pakt een blokje, verplaatst hem naar een bepaalde plaats en verplaatst de arm weer 
# terug naar boven de stapel. Je mag maximaal 25 regels code toevoegen.


# Jouw python instructies zet je vanaf hier:
def moveArm(direction:int, count:int)->int:
    for getal in range(count):
        if direction == "right":
            robotArm.moveRight()
        elif direction == "left":
            robotArm.moveLeft()

def moveBlock(direction:int, count:int)->int:
    robotArm.grab()
    moveArm(direction, count)
    robotArm.drop()
    for getal in range(count):
        if direction == "right":
            robotArm.moveLeft()
        elif direction == "left":
            robotArm.moveRight()


    


# Onderstaande code pas je niet aan
moveArm("right", 3)
moveBlock("left", 3)
moveBlock("right", 6)
moveBlock("right", 2)
moveBlock("right", 6)
moveBlock("left", 1)
moveBlock("left", 3)

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()