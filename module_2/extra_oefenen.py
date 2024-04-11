from time import sleep
from termcolor import colored
import os

getal = 1
os.system("cls")

# while True:
#     print(" ---------")
#     if getal == 1:
#         print(colored("|    O    |", "red")) ; sleep(1)
#         print("|    O    |") ; sleep(1)
#         print("|    O    |") ; sleep(1)
#     elif getal == 2:
#         print("|    O    |") ; sleep(1)
#         print("|    O    |") ; sleep(1)
#         print(colored("|    O    |", "green")) ; sleep(1)
#     elif getal == 3:
#         print("|    O    |") ; sleep(1)
#         print(colored("|    O    |", "yellow")) ; sleep(1)
#         print("|    O    |") ; sleep(1)
#     getal +=1
#     if getal > 3:
#         getal = 1
#     print(" ---------")

while True:
    print(" ---------")
    if getal == 1:
        print("|    O    |")
        print(colored("|    O    |", "yellow" "red"))
        print("|    O    |")
        print(" ---------")
    elif getal == 2:
        print("|    O    |")
        print(colored("|    O    |", "white"))
        print("|    O    |")
        print(" ---------")
    getal +=1
    if getal > 2:
        getal = 1
    sleep(1)
    os.system("cls")

