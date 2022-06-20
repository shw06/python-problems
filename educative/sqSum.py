# Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.


class Point:
    def __init__(self,x,y,z):  # passed parameters and assigned them to their corresponding properties.
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x**2 # calculated the squares of the properties and stored them in a variable.
        b = self.y**2
        c = self.z**2
        return (a + b + c) # Then, added all the squared numbers.Finally, returned their sum.


obj1 = Point(4,5,6)
print(obj1.sqSum())