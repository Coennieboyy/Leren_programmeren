from RobotArm import RobotArm

robotArm = RobotArm('toets-1')
robotArm.speed =2

# Jouw python instructies zet je vanaf hier:
def move_arm(direction:int, count:int)->int:
    for getal in range(count):
        if direction == "right":
            robotArm.moveRight()
        elif direction == "left":
            robotArm.moveLeft()

move_arm("right",4)

for j in range(2):
    robotArm.grab()
    for i in range(3):
            move_arm("left",2)
            robotArm.drop()
            if i <2:
                move_arm("right",2)
                robotArm.grab()

move_arm("right",5)

for j in range(2):
    robotArm.grab()
    for i in range(3):
            move_arm("right",2)
            robotArm.drop()
            if i <2:
                move_arm("left",2)
                robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()