from door import door
from functionList import *
import random


#  Instantiation of the prices to get
prices = ["Goat", "Goat", "Car"]
doors = fillDoors(prices) 
chosenDoor = chooseDoor(doors) # lets the player choose a door


input("\nOk. You've made your choice. Now I'm gonna open one of the other doors to see " +
        "what's behind. \nPress enter to continue")

otherDoors = [] #One of the other two doors gets opened which is suppost to hide a goat
for element in doors:
    if(element.getNumber != chosenDoor.getNumber):
        otherDoors.append(element)
       
for element in otherDoors:
    if(element.getPrice() != "Car"):
        element.openDoor()
        otherDoors.remove(element)



choice = keepOrChange(chosenDoor.getNumber(), otherDoors[0].getNumber()) # the user has the chance to change his decision

        
if (choice == chosenDoor.getNumber()):
    chosenDoor.openDoor()
else:
    otherDoors[0].openDoor()

input("Press Enter to exit....")
