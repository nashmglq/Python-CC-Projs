class Rectangle:

    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width
    
    def areaCalculation(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}")
    
    def perimeterCalculation(self):
        perimeter = 2 * (self.length + self.width)
        print(f"The perimeter is {perimeter}")




x = Rectangle(10,20)

print(x.length)
print(x.areaCalculation())
print(x.perimeterCalculation())