# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum

def sum(x,y,z):
    if x==y==z:
        return (3*(x+y+z))
    else :
        return (x+y+z)

x=int(input("enter number x:"))    
y=int(input("enter number y:"))    
z=int(input("enter number z:"))  
print(sum(x,y,z))  
