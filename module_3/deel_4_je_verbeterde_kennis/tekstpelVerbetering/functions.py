import time
import os
import keyboard

combat = 0

def ending(tekstEnding: str)-> str:
    if tekstEnding == "win":
        print('''
 __   __  _______  __   __    _     _  ___   __    _ 
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
|       ||  | |  ||  |_|  |  |       ||   | |       |
|_     _||  |_|  ||       |  |       ||   | |  _    |
  |   |  |       ||       |  |   _   ||   | | | |   |
  |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
    elif tekstEnding == "died":
        print('''
 __   __  _______  __   __    ______   ___   _______  ______   
|  | |  ||       ||  | |  |  |      | |   | |       ||      |  
|  |_|  ||   _   ||  | |  |  |  _    ||   | |    ___||  _    | 
|       ||  | |  ||  |_|  |  | | |   ||   | |   |___ | | |   | 
|_     _||  |_|  ||       |  | |_|   ||   | |    ___|| |_|   | 
  |   |  |       ||       |  |       ||   | |   |___ |       |     
  |___|  |_______||_______|  |______| |___| |_______||______|   ''')
    elif tekstEnding == "failed":
        print('''
 __   __  _______  __   __    _______  _______  ___   ___      _______  ______  
|  | |  ||       ||  | |  |  |       ||   _   ||   | |   |    |       ||      | 
|  |_|  ||   _   ||  | |  |  |    ___||  |_|  ||   | |   |    |    ___||  _    |
|       ||  | |  ||  |_|  |  |   |___ |       ||   | |   |    |   |___ | | |   |
|_     _||  |_|  ||       |  |    ___||       ||   | |   |___ |    ___|| |_|   |
  |   |  |       ||       |  |   |    |   _   ||   | |       ||   |___ |       |
  |___|  |_______||_______|  |___|    |__| |__||___| |_______||_______||______|''')
        
def slow_print(str):
    waitlist = [".", "!", "?"]
    for letter in str:
        if letter in waitlist:
            sleeptime = 0.3
        else:
            sleeptime = 0.05
        if keyboard.is_pressed('control'):  #* Controleer of de cntrol is ingedrukt
            print(letter, end='', flush=True)  #* Druk de letter direct af
        else:
            print(letter, end='', flush=True)
            time.sleep(sleeptime)
    print()


def clear_terminal(delay=0.0):
      time.sleep(delay)
      os.system('cls')

def ask_for_input(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 or user_input == 22446688:
                 return user_input
            if user_input != 1 or user_input != 2:
                 raise ValueError
        except ValueError:
            print("Ongeldige invoer. Voer 1 of 2 in.")
def ask_for_input_fight(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 or user_input == 3:
                 return user_input
            if user_input != 1 or user_input != 2 or user_input != 3:
                 raise ValueError
        except ValueError:
            print("Ongeldige invoer. Voer 1, 2 of 3 in.")
def ask_for_input_bewaker(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input == 1 or user_input == 2 and combat == 0 or user_input == 3 and combat == 1:
                 return user_input
            if user_input != 1 or user_input != 2 or user_input != 3:
                 raise ValueError
            if user_input == 3 and combat == 0:
                 slow_print("Je durft het niet")
        except ValueError:
            print("Ongeldige invoer. Voer 1 of 2 in.")