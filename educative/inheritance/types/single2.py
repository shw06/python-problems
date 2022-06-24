from traceback import print_tb


class Hospital:
    def names(self,name):
        self.name = name
        print("Name of the hospital: ", self.name)

class Department(Hospital):
    def depart(self,dept):
        self.dept = dept
        print("Department of: ", self.dept)

obj1 = Department()
obj1.names("City hospital")
obj1.depart("Neuro")