class Vehicle:
    def setTopSpeed(self,speed):
        self.topSpeed = speed
        print("The top speed is set to: ", self.topSpeed)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass


corolla = Car()
corolla.setTopSpeed(220)

volco = Truck()
volco.setTopSpeed(320)

