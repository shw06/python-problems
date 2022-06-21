class Student:
    def __init__(self,name,phy,chem,bio):  # initialized name, phy, chem, and bio as public properties in the class initializer.
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self): # defined the totalObtained() method. 
        return(self.phy + self.chem + self.bio) #In this method, added individual marks of all the subjects and returned the sum.

    def percentage(self):       # defined percentage(). In this method, called totalObtained() and used its value to calculate the percentage. 
        return((totalObtained / 300) * 100)    #300 is the total number of marks for a student
