class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def CalcArea(self):
        return self.length * self.width


rect = Rectangle(5, 3)


area = rect.CalcArea()
print(f"The area of the rectangle is: {area}")