import random

class Wardrobe:

    def __init__(self, name = '', material = ('wood', 'carbon fiber', 'glass'), open=bool, closed=bool, broken=bool):
        self.name = name
        self.material = material
        self.open = open
        self.closed = closed
        self.broken = broken


    def open_door(self):
        if self.open == True:
            print("The door is open")


    def close_door(self):
        if self.closed == True :
            print("The door is closed")
            Wardrobe.open_door(self)
            print("Now it is open")
        else:
            print("the door is open")


    def get_in(self):
        if self.open == True:
            print("The door is open, please come in.")
        else:
            print("The door is closed, please open the door.")
            Wardrobe.open_door(self)
            print("Now it is open, walk in.")

    def get_out(self):
        if self.open == True:
            print("The door is open, you can walk out.")
        else:
            print("The door is closed, you can not get out.")
            Wardrobe.open_door(self)
            print("Now it is open, walk on out.")


    def kick_it(self):
        if self.material == 'wood':
            print("I kicked {} and BAM it said".format(self.name))
        elif self.material == 'carbon fiber':
            print("I kicked {} and it said 'Thud'".format(self.name))
        elif self.material == 'glass':
            print("I kicked {} and BOOOOOOOM it broke".format(self.name))
            Wardrobe.broken == True
        else:
            raise ValueError('that is not a wardrobe')


    def until_it_brakes(self):
        while self.broken == False:
            self.broken = random.choice([True, False])
            Wardrobe.kick_it(self)
            print("Keep on kicking")





wardrobe1=Wardrobe('kassie', 'wood', open=False, closed=True, broken=False)
Wardrobe.until_it_brakes(wardrobe1)















