class Rectangle:
    def __init__(self,length,width):
        self.__length = length   # defined the initializer for the class and declared private properties – __length and __width – in it.
        self.__width = width

    def area(self):  # defined the method area() and returned the product of the two properties – __length and __width – in it.
        return (self.__length * self.__width)  

    def perimeter(self):  # defined the method perimeter() and returned twice the sum of the two properties – __length and __width – in it.
        return (2 * (self.__length + self.__width))

obj = Rectangle(4,5)  # defined a Rectangle class object, obj1, with properties 4 and 5

print("Area of a rectangle is: ",obj.area())  #  call the methods area() and perimeter() and print their values.
print("Perimeter of rectangle is: ",obj.perimeter())