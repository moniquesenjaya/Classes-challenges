import math

class Circle():

    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return ('Radius of circle is ' + str(self.getRadius()) + " and the color of circle is " + self.getColor())
    
    def getArea(self):
        return (math.pi * self.getRadius()**2)


class Cylinder(Circle):

    def __init__(self, height = 1.0, radius = 1.0, color = "red"):
        self.__height = height
        super().__init__(radius, color)
        
    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def __str__(self):
        return ('Radius of cylinder is ' + str(self.getRadius()) + ", the color of cylinder is " + self.getColor() + "and the height is " + str(self.getHeight()))

    def getVolume(self):
        return (self.getArea() * self.__height)

circle = Circle()
cylinder = Cylinder()

