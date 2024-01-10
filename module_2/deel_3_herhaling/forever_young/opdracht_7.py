from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.reportFlaws = False
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(5):
    for j in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if i < 4:
        robotArm.moveRight()
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()