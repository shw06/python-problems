class Hospital:
    def __init__(self,name,doctor):
        self.name = name
        self.doctor = doctor

    def printHospital(self):
        print("Hospital name: ", self.name)
        print("Doctor name: ",self.doctor)

class Department(Hospital):
    def __init__(self, name, doctor,dname):   # constructor for child class
        Hospital.__init__(self,name,doctor)    # constructor of parent class
        self.dname = dname

    def printHospitalDept(self):
        self.printHospital()
        print("Department name: ", self.dname)

obj1 = Department("City Hospital","Dr. Evans","Dept of Cardiology")
obj1.printHospitalDept()
