from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')
#RobotArm.moveRight()
#RobotArm.moveLeft()
#RobotArm.grab()
#RobotArm.drop()
# Jouw python instructies zet je vanaf hier:
robotArm.reportFlaws = False
robotArm.speed = 4
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()