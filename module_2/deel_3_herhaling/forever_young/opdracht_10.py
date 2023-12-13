from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.reportFlaws = False
robotArm.speed = 3
hvr = 10
# Jouw python instructies zet je vanaf hier:
for i in range(5):
    for a in range(1):
        robotArm.grab()
        hvr -=1
        for b in range(hvr):
            robotArm.moveRight()
        robotArm.drop()
        hvr -=1
        for c in range(hvr):
            robotArm.moveLeft()





    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()