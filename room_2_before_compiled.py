import random
import os
clear = lambda: os.system('cls')
clear()
rand_num = random.randint(0,100)
door_key = False

def room2():
    global door_key
    global rand_num
    i=0
    while i <2:
        print("\nPick one of the following options: \n 1. Look at the windows  \n 2. Try to open the door \n 3. Turning back")
        choice = input()
        #Window option
        if choice == "1":
            clear()
            print("You look outside the window and see the dark abyss below and a steep ledge leading to another room do you attempt to cross?")
            print("Pick one of the following options: \n 1. Yes (10% chance of succeeding)  \n 2. No")
            window_choice = input()
            clear()
            if window_choice == "1" and rand_num <=10:
                print("You have safely crossed the ledge and entered a new room.")
                print("You find an elevator and enter it....") #finish later
            elif window_choice == "1" and rand_num >10:
                print("You took your chances and have fallen into the abyss")
                #go to room1{}
                break
            elif window_choice == "2": 
                clear()
                print("You decided to leave the window and headed back to the centre of the room")
            else:
                clear()
                print("You inputted the wrong number, please refer to the list")
        #Door option
        elif choice == "2":
            clear()
            print("Pick one of the following options: \n 1. Attempt to open the door  \n 2. Forcing the door to open with brute force")
            door_choice= input()
            clear()
            if door_choice == "1" and door_key == True:
                print("You used the key you found earlier from the drawer and the door opened")
                #go to room 3
            elif door_choice == "1" and door_key == False:
                print("The door is locked, maybe there is a key hidden somewhere in this room")
            elif door_choice == "2":
                print("You managed to forcefully open the door and take two steps into the room.")
                print("You hear the floorboard squeak and then a beast rip it's apart and drags you into the abyss")
                #run code to go to room 1
                break
            else:
                print("You inputted the wrong number, please refer to the list")
        #Drawer options
        elif choice == "3":
            clear()
            print("You turn and look behind you and see drawers")
            clear()
            print("Pick one of the following options: \n 1. Search the drawers  \n 2. Ignore the drawers")
            drawer_choice = input()
            clear()
            if drawer_choice == "1" and door_key == False:
                door_key = True
                print("You search the drawer and managed to find a key lying there and picked it up.")
            elif drawer_choice == "1" and door_key == True:
                print("You already searched and found a key here before")
            elif drawer_choice== "2":
                print("You see the drawers but decided to leave it alone.")
            else:
                print("You inputted the wrong number, please refer to the list")
        else:
            clear()
            print("You inputted the wrong number, please refer to the list")

room2()