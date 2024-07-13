# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

import datetime
exam_st_date = (11, 12, 2014)
day,month,year = exam_st_date
date=datetime.datetime(year,month,day)
print(date.strftime("%Y-%m-%d"))


