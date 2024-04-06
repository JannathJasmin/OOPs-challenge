# 1.Create a class named person and return how many objects are created for that class
class Person:
    count = 0

    def __init__(self):
        Person.count += 1
person1 = Person()
person2 = Person()
person3 = Person()
print("Number of person objects created:", Person.count)

# 2.Create a class student with attributes names and marks**
 
#  a. Create a method to display name and mark of a student
 
#  b. Create a method to show the grades of a student in the following manner
#  * marks>=60: First Class
#  * marks>=50: Second Class
#  * Else Failed

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    
    def calculate_grade(self):
        if self.marks >= 60:
            print("Grade: First Class")
        elif self.marks >= 50:
            print("Grade: Second Class")
        else:
            print("Grade: Failed")
name = input("Enter student's name: ")
marks = int(input("Enter student's marks: "))
student = Student(name, marks)
student.calculate_grade()
student.display_info()
student.calculate_grade()

# Encapsulation
# 3. Create a rectangle class with a private variables height and widht and find the area using the area method
class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width
rectangle1 = Rectangle(5, 4)
print("Area of rectangle1:", rectangle1.area())

# 4.Inheritance Problem and Encapsulation
# 1. Create a  parent class called "shape" which has attributes color and filled, color takes default value as black and filled take default boolean value. Use get_color, get_filled to set the value of color and filled and set_color,get_filled to get the value of color and filled
class Shape:
    def __init__(self, color='black', filled=False):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled
if __name__ == "__main__":
    # Creating an instance of Shape
    my_shape = Shape()

    # Getting default values
    print("Default color:", my_shape.get_color())
    print("Default filled:", my_shape.get_filled())

    # Setting new values
    my_shape.set_color('red')
    my_shape.set_filled(True)

    # Getting updated values
    print("Updated color:", my_shape.get_color())
    print("Updated filled:", my_shape.get_filled())

# 2. Create child class called Rectangle for the class "shape" and which takes the argument length,breadth 
#  * Set the value of both length and breadth using set method and get method
#  * Find the area and perimeter of rectangle using get_area and get_perimeter methods

class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def set_dimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
rectangle = Rectangle(5, 4)
print("Area:", rectangle.get_area())
print("Perimeter:", rectangle.get_perimeter())

# 3.Create another child class called Circle for the class "shape" which takes the argument radius
#  * Set the value of radius using set method
#  * Get the value of radius using get method
#  * Use get_area and get_perimeter to find the area and perimeter of the circle
import math
class Shape:
    def __init__(self):
        pass
    
    def get_area(self):
        pass
    
    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def set_radius(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
circle = Circle(5)
print("Radius of the circle:", circle.get_radius())
print("Area of the circle:", circle.get_area())
print("Perimeter of the circle:", circle.get_perimeter())

# 5.ABSTRACT METHOD
# 1. Create a abstract class named Shape with abstract methods area and perimeter
from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass
    def perimeter(self):
        pass
# 2. Create two class named Square and Rectangle which inherit the shape class and define area and perimeter methods
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
# 6.Determine if a triangle is equilateral, isosceles, or scalene.

    # * An equilateral triangle has all three sides the same length.

    # * An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

    # * A scalene triangle has all sides of different lengths
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

triangle = triangle_type(side1, side2, side3)
print("The triangle is", triangle)
