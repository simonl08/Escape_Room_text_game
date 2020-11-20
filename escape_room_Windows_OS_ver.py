import random
import time
import sys
import os
from sys import platform

clear = lambda: os.system('cls')
clear()
rand_num = random.randint(0,100)
door_key = False
silver_dollar = False

key1 = 0
key2 = 0

def delay_print03(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
def delay_print01(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

while True:
    def room1():
        global key1
        key1 = 0
        global key2
        key2 = 0
        global silver_dollar
        silver_dollar = False
        global door_key
        door_key = False
        delay_print03("ESCAPE ROOM TEXT GAME")
        delay_print03("\nYou wake up in an unfamiliar room.")
        delay_print03("\n1. GET UP\n")
        option0 = int(input())
        if option0 == 1: #Getting up
            clear()
            room1_1()
        else:
            delay_print03("Wrong Key Press\n")
            clear()
            room1()

    def room1_1():
        delay_print03("There's a door opposite your bed.")
        delay_print03("\n1. TRY THE DOOR")
        delay_print03("\n2. LOOK AROUND\n")
        option1 = int(input())
        if option1 == 1: #Player has opened the door
            clear()
            delay_print03("You have opened the door and have entered a new room.")
            delay_print03("\nHere you see a window and a door")
            room2()
        elif option1 == 2: #Player is looking around
            clear()
            delay_print03("You're surrounded by walls engorged in damp. An old faded painting hangs on one of them.")
            delay_print03("\nBeyond the walls, you hear movement. You need to get out of here.")
            delay_print03("\n1. TRY THE DOOR")
            delay_print03("\n2. INSPECT THE PAINTING \n")
            option2 = int(input())
            if option2 == 1: #Going for the door
                clear()
                delay_print03("\nYou have opened the door and have entered a new room\n")
                delay_print03("Here you see a window and a door")
                room2()
            elif option2 == 2: #Inspecting the painting
                clear()
                delay_print03("Stop wasting time. Get moving.")
                delay_print03("\n1. TRY THE DOOR \n")
                option3 = int(input())
                if option3 == 1:
                    clear()
                    delay_print03("You have opened the door and have entered a new room\n")
                    delay_print03("Here you see a window and a door")
                    room2()
                else:
                    clear()
                    delay_print03("\nWrong Key Press")
                    room1_1()
            else:
                clear()
                delay_print03("\nWrong Key Press")
                room1_1()
        else:
            clear()
            delay_print03("\nWrong Key Press")
            room1_1()

    def room2():
        global door_key
        global rand_num
        i=0
        while i < 1:
            delay_print03("\n1. LOOK AT THE WINDOWS  \n2. TRY TO OPEN THE DOOR \n3. TURNING BACK \n")
            choice = int(input())
            #Window option
            if choice == 1:
                clear()
                delay_print03("You look outside the window and see the dark abyss below and a steep ledge leading to another room. \nDo you attempt to cross?")
                delay_print03("\n1. YES (10% CHANCE OF SUCCESS)  \n2. NO \n")
                window_choice = int(input())
                clear()
                if window_choice == 1 and rand_num <=10:
                    delay_print03("You have safely crossed the ledge and entered a new room.")
                    delay_print03("\nYou find an elevator and enter it....") #finish later
                    delay_print03("You've left the building, you look down on the floor and find $5. \nYou decide to go get yourself a strawberry milkshake")
                    delay_print03("\nYou've won.")
                    i += 1
                    break
                elif window_choice == 1 and rand_num >10:
                    delay_print03("You took your chances and have fallen into the abyss.\n")
                    #go to room1{}
                    room1()
                elif window_choice == 2: 
                    clear()
                    delay_print03("\nYou decided to leave the window and headed back to the centre of the room")
                else:
                    clear()
                    delay_print03("\nWrong Key Press.")
            #Door option
            elif choice == 2:
                clear()
                delay_print03("You walk to the door.")
                delay_print03("\n1. ATTEMPT TO OPEN THE DOOR  \n2. FORCE THE DOOR OPEN\n")
                door_choice= int(input())
                clear()
                if door_choice == 1 and door_key == True:
                    delay_print03("You used the key you found earlier from the drawer and the door opened")
                    i += 1
                       
                    room3()
                    #go to room 3
                elif door_choice == 1 and door_key == False:
                    delay_print03("\nThe door is locked, maybe there is a key hidden somewhere in this room")
                elif door_choice == 2:
                    delay_print03("You managed to forcefully open the door and take two steps into the next room.")
                    delay_print03("\nYou hear the floorboard squeak and then a giant mouldy strawberry rips it apart and drags you into the abyss\n")
                    #run code to go to room 1
                    room1()
                else:
                    delay_print03("\nWrong Key Press")
            #Drawer options
            elif choice == 3:
                clear()
                delay_print03("You turn and look behind you and see drawers")
                delay_print03("\n1. SEARCH THE DRAWERS  \n2. IGNORE THE DRAWERS\n")
                drawer_choice = int(input())
                clear()
                if drawer_choice == 1 and door_key == False:
                    door_key = True
                    delay_print03("You search through all the drawers and just as it seemed that there's nothing to find, you managed to spot a key lying there. \nIt might be useful.")
                elif drawer_choice == 1 and door_key == True:
                    delay_print03("\nYou already searched and found a key here before")
                elif drawer_choice== 2:
                    delay_print03("You see the drawers but decided to leave it alone.")
                else:
                    delay_print03("\nWrong Key Press")
            else:
                clear()
                delay_print03("\nWrong Key Press")

    def room3():
        global key1
        global key2
        i = 0
        delay_print01("\nThe door is unlocked. \nYou turn the handle, and it slowly creeks open, sending a shiver down your spine. \nYou slowly enter, and look around. \nAhead of you, you see a large door. \nTo your left, there is a wardrobe covered in what appears to be some sort of... red slime? \nNext to the wardrobe is a large sofa, with a mirror on the wall above, surrounded by more of that red slime. \nTo your right, a magnificent, old mantelpiece. \nThe fireplace is boarded up. \nThere is an unpleasant, fruity smell in the air. \nYou take a deep breath and...")
        while i < 1: # GAME LOOP - REVERTS BACK TO HERE IF PLAYER DOESN'T ESCAPE OR GETS KILLED

            options = [                     #delay_print03 a\n list which can be appended with options that only become available when certain parameters have been met (ie. both keys are found)
            "\n1. TRY THE DOOR",
            "\n2. INSPECT THE WARDROBE",
            "\n3. LOOK AT THE SOFA",
            "\n4. CHECK THE MANTELPIECE \n"
                ]
            for choice in options:
                delay_print03(choice)
            user_choice = int(input())                
            if user_choice == 1: # door
                if key1 + key2 != 2: # doesn't have keys
                    clear()
                    delay_print03("\nThe door is locked tight and won't open. There are two locks.")
                else: # has keys
                    clear() 
                    delay_print03("You unlock the door with the two keys, and enter a fourth room... \nYou see a bed, with a loft door in the ceiling.")
                    i += 1
                    room4()
            elif user_choice == 2: # wardrobe
                clear()
                delay_print03("The wardrobe is worn, and the wood is split. As you open the door, it feels like it will crumble in your hand. \nInside... it's empty. Just a selection of smelly, old clothes, riddled in mothballs. \nThe stench is overpowing, you close the door and look back to the room.")
            elif user_choice == 3: # sofa
                clear()
                delay_print03("The cushions are strewn all over the place. Do you:\n")# one cushion out of place. go to place it back? if yes, see a key. if no, look elsewhere.")
                cushion = int(input("1. REPLACE THE CUSHIONS.\n2. TURN BACK.\n"))
                if cushion == 1 and key1 == 1:
                    clear()
                    delay_print03("You have already done this, and found a key. Maybe try something else?")
                elif cushion == 1: 
                    clear()
                    delay_print03("You replace the cushions and find a key. You turn back to the room.")
                    key1 += 1
                elif cushion ==2:
                    clear()

                else:
                    clear()
                    delay_print03("\nWrong Key Press")
            elif user_choice == 4 and key2 == 1:
                clear()
                delay_print03("You have already done this, and found a key. Maybe try something else?")

            elif user_choice == 4: # mantelpiece
                clear()
                key2 += 1
                delay_print03("You walk over to the mantelpiece. \nThe fireplace is all boarded up, but there is a small hole to the bottom corner of the board. \nOn further inspection, you find a key. \nYou turn back to the room.")
            else:
                clear()
                delay_print03("\nWrong Key Press.")


    def room4():
        global silver_dollar        
        
        delay_print03("\n1. SEARCH THE BEDDING \n2. TRY THE LOFT DOOR \n3. MOVE THE BED TO THE LOFT DOOR \n")

        option2 = int(input())

            
        if option2 == 1 and silver_dollar == True:
            clear()
            delay_print03("You've already checked the bedding")
            room4()
        elif option2 == 1: #Player has Searched Bedding
            clear()
            delay_print03("You check under the pillow and find an old silver dollar.\n")
            delay_print03("You return to the door you had used to enter.")
            silver_dollar = True
            room4()
                   
        elif option2 == 2: #Player has tried to open the loft door iteration 2
            clear()
            delay_print03("It's too high to reach.")  #player has tried to open the loft door
            room4()
            
        elif option2 ==3 and silver_dollar == True:
            clear()
            delay_print03("You move the bed towards the loft door")
            delay_print03("\n1. GET ON THE BED AND TRY TO OPEN THE LOFT DOOR \n2. TURN BACK\n")
            option3 = int(input())
                

            if option3 == 1:
                clear()
                delay_print03("The door opens. It's Strawberry Steve. He grabs you and hauls you into the crawl space.") #Character has died reset
                delay_print03("\nYOU HAVE DIED \n\n\n\n")
                room1()
                
            elif option3 == 2:
                clear()
                delay_print03("You see a sizeable vent in the corner of the room. \nIt's screwed to the wall, but not too tightly")
                delay_print03("\n1. TRY USING THE SILVER DOLLAR TO UNSCREW THE VENT\n")

                sdp = int(input())
                if sdp == 1:
                    clear()
                    delay_print03("The coin slots easily into the grooves of the screws. \nYou unwind them from the wall and the vent grate falls to the ground. \nYou scrape through to the other side, and find yourself breathing fresh air. \nYou are outside. You are free. \nYou hear unearthly noises from the house behind you. \n\n\nRUN.")   
                else:
                    clear()     
                    delay_print03("Wrong Key Press")
                    room4()
                        
            else:
                clear()
                delay_print03("Wrong Key Press")
                room4()


        elif option2 == 3: #Player has moved the bed to the loft door  
            clear()
            delay_print03("You move the bed towards the loft door\n")
            delay_print03("1. GET ON THE BED AND TRY TO OPEN THE LOFT DOOR \n2. PUT THE BED BACK\n")
            option3 = int(input())

            if option3 == 1: #Player has opened the loft door
                clear()
                delay_print03("The door opens. It's a giant mouldy strawberry. It grabs you and hauls you up the ladder.") #Character has died reset
                delay_print03("YOU HAVE DIED \n\n\n\n")
                room1()
            elif option3 == 2: #Player has turned back
                clear()
                delay_print03("You've put the bed back to it's original spot")
                room4()
            else:
                clear()
                delay_print03("Wrong Key Press")
                room4()

        else: #if option 2 fails
            clear()
            delay_print03("Wrong Key Press")
            room4() 
    
    break
room1()