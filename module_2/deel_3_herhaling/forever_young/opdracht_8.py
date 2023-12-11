from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.reportFlaws = False
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for j in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for a in range(8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()