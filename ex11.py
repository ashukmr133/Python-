# Write a Python program to calculate the number of days between two dates.
from datetime import datetime

def diff(date1,date2):
    date1=datetime.strptime(date1,"%Y-%m-%d")
    date2=datetime.strptime(date2,"%Y-%m-%d")
    d=abs(date2-date1)
    print("diff=" ,d)


date1=input("date1 (YYYY-MM-DD)")    
date2=input("date2 (YYYY-MM-DD)")    
diff(date1,date2)