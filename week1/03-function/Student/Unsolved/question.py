#TODO convert the following code by using function calculate_distance
import math

#test input
#x1 = 0 
#y1 = 0
#x2 = 4
#y2 = 3

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance between the two points is ", distance)

#TODO-Add your function calculate_distance here, call the function
# and get the distance between the two points