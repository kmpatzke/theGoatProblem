
import random
from door import door



def fillDoors(prices):
    doors = []

    counter = 1
    while(len(prices) != 0):
        ranIndex = random.randrange(0, len(prices))
        doors.append(door(counter, prices[ranIndex]))
        del prices[ranIndex]
        counter += 1
   
    return doors



def chooseDoor(array):
    chosenIndex = random.randrange(0, 3)    
    return array[chosenIndex]



def keepOrChange(chosenDoorNr, otherDoorNr):
    choice = otherDoorNr
    return choice
