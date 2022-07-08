from math import pi
#Rectangles       A = length * wwidth
def rectangle():
    length = int(input("Enter the side:"))
    width = int(input("Enter the side:"))
    Area = length * width
    print("Area of the Rectangle="+str(Area))


#Circles          A = pi * r * 2
def circle():
    r = int(input("Enter the side:"))
    Area = pi * r * 2
    print("Area of the Circle="+str(Area))