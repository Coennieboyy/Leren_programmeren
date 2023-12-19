from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.reportFlaws = False
robotArm.speed = 3
arm = 1
gebleven = 0
# Jouw python instructies zet je vanaf hier:
for a in range(8):
    robotArm.moveRight()
    arm += 1
for b in range(9):
    robotArm.grab()
    gebleven = arm
    kleur = robotArm.scan()
    if kleur != "red":
        robotArm.drop()
    else:
        for c in range (10 - arm):
            robotArm.moveRight()    
            arm += 1
        robotArm.drop()
        for d in range(10 - gebleven):
            robotArm.moveLeft()
            arm -= 1
    if b < 8:
        robotArm.moveLeft()
        arm -= 1
        





    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()