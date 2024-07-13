# Write a Python program to display the current date and time.

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%y-%m-%d %H:%M:%S")
print(current_time)