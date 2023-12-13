from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.reportFlaws = False
robotArm.speed = 3
blokje=0
# Jouw python instructies zet je vanaf hier:
while True:
    robotArm.grab()
    kleur = robotArm.scan()
    blokje +=1
    if kleur != "":  
        for a in range(blokje):
            robotArm.moveRight()
        robotArm.drop()
        for b in range(blokje):
            robotArm.moveLeft()
    else:
        break


        





    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()