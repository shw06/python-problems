from turtle import color


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def printDetails(self):
        print("Car capacity: ",self.capacity)


class Tires:
    def __init__(self,tires = 0):
        self.tires = tires

    def printDetails(self):
        print("Tires: ",self.tires)

class Doors:
    def __init__(self,doors = 0):
        self.doors = doors

    def printDetails(self):
        print("Doors: ",self.doors)

class Car:
    def __init__(self,eng,tr,dr,color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Color: ",self.color)


c = Car(1600,4,2,"Blue")
c.printDetails()