# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

def diff(n):
    if n>17:
        return abs(2*(n-17))
    else:
        return (17-n)
    
n=int(input("enter number:"))
print(diff(n))


