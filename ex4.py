#Write a Python program that calculates the area of a circle based on the radius entered by the user.

import math
r= float(input("enter radius:"))
area=  math.pi*(r**2)
area=round(area,3)
print("area = ",area)