class Power:
    def setPower(self,power):
        self.power = power

class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine, Power):
    def printDetails(self):
        print("Power: ", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setPower("2000cc")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()