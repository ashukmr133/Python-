# Write a Python program that prints the calendar for a given month and year.

import calendar


def calender(year,month):
    cal=calendar.year(year,month)
    print(cal)

year=int(input("enter year:"))
month=int(input("\n enter month:"))
calender(year,month)