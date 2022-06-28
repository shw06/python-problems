# Override a Method Using the Super Function

class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname

class Xshape(Shape):
    def __init__(self, name):
        self.xname = name

    def getName(self):
        return (super().getName()+ ','+self.xname)

circle = Xshape("Circle")
print(circle.getName())

