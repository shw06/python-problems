class Student:   #implemented the Student class, which has two private properties – __name and __rollNumber – 
                 # that are initialized in the set methods.
    __name = None
    __rollNumber = None
    
    def setName(self, name):  # implemented setName(name), a method that sets the __name property.
        self.__name = name

    def getName(self):  #  implemented getName(), a method that returns the __name property.
        return self.__name

    def setRollNumber(self, rollNumber):  # implemented setRollNumber(RollNumber), a method that sets the __rollNumber property.
        self.__rollNumber = rollNumber

    def getRollNumber(self):  #  implemented getRollNumber(), a method that returns the __rollNumber property
        return self.__rollNumber

obj = Student()
obj.setName("Alex")
print("Name: ",obj.getName())
obj.setRollNumber("3529")
print("Roll number: ",obj.getRollNumber())



    