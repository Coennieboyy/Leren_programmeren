from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.reportFlaws = False
robotArm.speed = 1
blokje = 1
# Jouw python instructies zet je vanaf hier:
for i in range(4):
    for a in range(blokje):
        robotArm.grab()
        for o in range(5):
            robotArm.moveRight()
        robotArm.drop() 
        for p in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    blokje +=1  
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()