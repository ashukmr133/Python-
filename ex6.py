# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
a=input("input csv values:")
l=a.split(",")
t=tuple(l)
print(l,"\n",t)