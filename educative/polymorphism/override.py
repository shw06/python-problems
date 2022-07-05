# Override a Method Using the Super Function

# Parent Class
class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname


# child class
class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + ", " + self.xsname)


circle = XShape("Circle")
print(circle.getName())

