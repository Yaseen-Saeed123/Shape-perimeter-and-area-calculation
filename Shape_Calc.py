from abc import ABC, abstractmethod
import math

# Create abstract class
class Shape(ABC):
    @abstractmethod
    def area():
        ...

    @abstractmethod
    def perimeter():
        ...

    @abstractmethod
    def display(self):
        return f"Area = {self.area()} square cm \nPermeter = {self.perimeter()} cm"

# Create class for each shape
class Square(Shape):
    def __init__(self, side=None, diagonal=None):
        if diagonal is None:
            self.__side = side
        elif side is None and diagonal is not None:
            self.__side = diagonal / math.sqrt(2)

    def area(self):
        return round(self.__side ** 2, 2)
    
    def perimeter(self):
        self.perimeter_used = True
        return round(self.__side * 4, 2)
    
    def display(self):
        string = super().display()
        return f"side = {round(self.__side)} cm\n" + string

class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return round(self.__length * self.__width, 2)
    
    def perimeter(self):
        return round((self.__length + self.__width) * 2, 2)
    
    def display(self):
        string = super().display()
        return f"Length = {self.__length} cm \nWidth = {self.__width} cm\n"+ string

class Circle(Shape):
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.__radius = radius
        elif radius is None and diameter is not None:
            self.__radius = diameter / 2

    def area(self):
        return round(math.pi * self.__radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * self.__radius * math.pi, 2)
    
    def display(self):
        string = super().display()
        return f"radius = {round(self.__radius)} cm\n" + string

class Parallelogram(Shape):
    def __init__(self, base_1=None, base_2=None, height_1=None):
        self.__base_1 = base_1
        self.__base_2 = base_2
        self.__height_1 = height_1

    def area(self):
        return round(self.__base_1 * self.__height_1, 2)
    
    def perimeter(self):
        return round((self.__base_1 + self.__base_2) * 2, 2)
    
    def display(self):
        string = super().display()
        return f"First base = {self.__base_1} cm \nSecond base = {self.__base_2} cm \nHeight corresponding to first base = {self.__height_1} cm\n" + string

# Main program
print("-"*30)
shape = input("What shape do You want to measure its perimeter and area? ").lower().strip()
print("-"*30)
if shape == "square":
    try:
        s_or_d = input("Do you want perimeter and area by side or by diagonal? ").lower().strip()
        print("-"*30)
        if s_or_d == "side":
            side = int(input("Please enter side length in cm. ").lower().strip())
            print("-"*30)
            square = Square(side=side)
            print(square.display())
            print("-"*30)
        elif s_or_d == "diagonal":
            diagonal = int(input("Please enter diagonal length in cm. ").lower().strip())
            print("-"*30)
            square = Square(diagonal=diagonal)
            print(square.display())
            print("-"*30)
    except ValueError:
        print("-"*30)
        print("Can't calculate")
        print("-"*30)

elif shape == "rectangle":
    try:
        length = int(input("Please enter length in cm. ").lower().strip())
        print("-"*30)
        width = int(input("Please enter width in cm. ").lower().strip())
        print("-"*30)
        rect = Rect(length=length, width=width)
        print(rect.display())
        print("-"*30)
    except ValueError:
        print("-"*30)
        print("Can't calculate")
        print("-"*30)

elif shape == "circle":
    d_or_r = input("Will you enter diameter or radius? ").lower().strip()
    print("-"*30)
    if d_or_r == "diameter":
        try:
            diameter = int(input("Please enter diameter in cm. ").lower().strip())
            print("-"*30)
            circle = Circle(diameter=diameter)
            print(circle.display())
            print("-"*30)
        except ValueError:
            print("-"*30)
            print("Can't calculate")
            print("-"*30)
    elif d_or_r == "radius":
        try:
            radius = int(input("Please enter radius in cm. ").lower().strip())
            print("-"*30)
            circle = Circle(radius=radius)
            print(circle.display())
            print("-"*30)
        except ValueError:
            print("-"*30)
            print("Can't calculate")
            print("-"*30)
    else:
        print("Wrong Either diameter or radius")

elif shape == "parallelogram":
    try:
        base_1 = int(input("Please enter first base in cm. ").lower().strip())
        print("-"*30)
        base_2 = int(input("Please enter second base in cm. ").lower().strip())
        print("-"*30)
        height_1 = int(input("Please enter the height corresponding to first base in cm. ").lower().strip())
        print("-"*30)
        parallel = Parallelogram(base_1=base_1, base_2=base_2, height_1=height_1)
        print(parallel.display())
        print("-"*30)
    except ValueError:
        print("-"*30)
        print("Can't calculate")
        print("-"*30)        