from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.reportFlaws = False
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for a in range(8):
    robotArm.moveRight()
for b in range(9):
    for i in range(1):
        robotArm.grab()
        kleur = robotArm.scan()
        if kleur != "white":
            robotArm.drop()
        else:
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
    if b < 8:
        robotArm.moveLeft()
        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()