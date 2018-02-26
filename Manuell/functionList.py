import random
from door import door


# randomly puts two goats and one car behind the doors
def fillDoors(prices):
    doors = []

    counter = 1
    while(len(prices) != 0):
        ranIndex = random.randrange(0, len(prices))
        doors.append(door(counter, prices[ranIndex]))
        del prices[ranIndex]
        counter += 1
   
    return doors


# lets the player choose his door
def chooseDoor(array):
    chosenIndex = None
    while(True):
    
        try: # the input must be an int and > 0 and < 4 
            chosenIndex = int(input("\nYou see three doors. One is hiding a car " +
                                        "but behind the other two a goat is" +
                                         "waiting for you. Choose. 1, 2 or 3: ")) 
        except:
            print("Oops. Invalid value. Please try again.")
            continue
        if(0 < chosenIndex < 4):
            break
        else:
            print("Your number has to be 1, 2 or 3. Please try again")
            continue
    return array[chosenIndex - 1]


#lets the player dicide weather to stick to his choice or not
def keepOrChange(chosenDoorNr, otherDoorNr):
    choice = None
    chosenNr = chosenDoorNr
    otherNr = otherDoorNr

    while(True):
        choice = input("\nDo you want to stick to door #{} or change to door #{} ? {}: Stay {}: Change : ".format(chosenDoorNr, otherNr, chosenDoorNr, otherNr))
        try:
            choice = int(choice)
        except:
            print("Oops. Invalid value. Please try again.")
            continue
        if(choice == chosenDoorNr or choice == otherDoorNr):
            break
        else:
            print("Your number has to be {} or {}. Please try again".format(chosenDoorNr, otherDoorNr))
            continue
        return choice
