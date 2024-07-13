# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_1000_2000(n):
    if abs(1000-n)<=100 or abs(2000-n)<=100:
        return 1
    else :
        return 0
    
n=int(input("enter number:"))
print(bool(near_1000_2000(n)))    
    
    
