class Hospital:
    def name(self, name):
        self.name = name
        print("name of the hospital is : ", self.name)

class Department(Hospital):
    def dept(self, department):
        self.dept = department
        print("Department of :", self.dept)

class Doctor(Department):
    def who(self,doctor):
        self.who = doctor
        print("Doctor: ", self.who)


Misc = Doctor()
Misc.name("City Hospital")
Misc.dept("Pediatrics")
Misc.who("Mr. Smith")
