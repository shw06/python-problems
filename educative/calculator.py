class Calculator:
    def __init__(self,num1,num2):   # have implemented the Calculator class, which has the two properties, num1 and num2
        self.num1 = num1
        self.num2 = num2        

    def add(self):
        return(self.num2 + self.num1)   #implemented add(), a method that returns the sum, num1 + num2, of both properties.

    def subtract(self):
        return(self.num2 - self.num1)   #implemented subtract(), a method that returns the subtraction of num1 from num2

    def multiply(self):
        return(self.num2 * self.num1)   #  implemented multiply(), a method that returns the product, num2 \times num1, of both properties.

    def divide(self):
        return(self.num2 / self.num1)   # implemented divide(), a method that returns the division of num2 by num1.

new_obj = Calculator(10, 94)
print("Addition: ",new_obj.add())
print("Substraction: ",new_obj.subtract())
print("Multiplication: ",new_obj.multiply())
print("Division: ",new_obj.divide())

