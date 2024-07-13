# Write a Python program to get the volume of a sphere with radius six.

import math

def volume(r):
    v=round((4/3)*(math.pi * (r**3) ),3)
    return v

r=float(input("enter radius:"))
print(volume(r))