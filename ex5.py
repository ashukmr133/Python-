#  Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

name=input("enter user's name:")
# a="Ashutosh Kumar"
name=name.split()
# fn=b[0]
# ln=b[1]
reversed_name=name[::-1]
reversed_full_name = " ".join(reversed_name)
print(reversed_full_name)