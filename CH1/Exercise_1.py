#Import Library
import math

#Input for radius
radius = int(input("Enter radius of a circle: "))

#Function and calculation
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

#Print Result
print("The circumferences is: " ,circumference, \
", and the area is: ", area)
