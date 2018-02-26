
class door:
    def __init__(self, number, price ):
        self.__number = number
        self.__price = price

    def getNumber(self):
        return self.__number
    def getPrice(self):
        return self.__price
    def openDoor(self):
        print("Door #{} opened. It is ..... a {}.".format(self.__number, self.__price))



            
       
