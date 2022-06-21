class Student:
    __name = None
    __rollNumber = None
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

obj = Student()
obj.setName("Alex")
print("Name: ",obj.getName())
obj.setRollNumber("3529")
print("Roll number: ",obj.getRollNumber())



    