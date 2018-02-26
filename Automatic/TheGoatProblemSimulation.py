from door import door
from functionList import *
import random

def main():
    while True:
        rounds = int(input("How many rounds you want to simulate?"))
        try:
            rounds = int(rounds)
            break
        except ValueError:
            print("Oooops. Invalid value")

    hits = 0

    for i in range(rounds):
        #  Instantiation of the prices to get
        prices = ["Goat", "Goat", "Car"]


        doors = fillDoors(prices) # filled in the next step
        chosenDoor = chooseDoor(doors) # lets the player choose a door / In the simulation mode a random door gets picked



        otherDoors = [] #One of the other two doors gets opened which is suppost to hide a goat
        for element in doors:
            if(element.getNumber != chosenDoor.getNumber):
                otherDoors.append(element)
       
        for element in otherDoors:
            if(element.getPrice() != "Car"):
                otherDoors.remove(element)



        choice = keepOrChange(chosenDoor.getNumber(), otherDoors[0].getNumber()) # the user has the chance to change his decision/ In simulation mode the door always be changed

        
        otherDoors[0].openDoor()
        if(otherDoors[0].getPrice() == "Car"):
            hits += 1
        

    


    print("The hit rate is {}%".format(hits/ rounds * 100))
if __name__ == "__main__":
    main()
    input("Press Enter to Exit.....")

