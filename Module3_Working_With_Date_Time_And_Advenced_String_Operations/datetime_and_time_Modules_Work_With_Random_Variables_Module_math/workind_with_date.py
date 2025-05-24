from datetime import datetime 

now = datetime.now()
print(f"datetime.now():\n{now}")

print(f"\nMethod call:\n{now.year}")
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.tzinfo)



# The datetime object has methods to get the date (without time) and time (without date):
print(f"\n.date(): {now.date()}")
print(f".time(): {now.time()}")



import datetime

# Combining date and time into a single datetime object
date_part = datetime.date(5923, 12, 22)
time_part = datetime.time(15, 54, 22)

combine_datetime = datetime.datetime.combine(date_part, time_part)
print(f".combine(): {combine_datetime}")



# To create a datetime object with a specific date:
specific_date = datetime.datetime(year=9361, month=4, day=5, hour=17, minute=41, second=59, microsecond=9999)

print(f"\nspecific_date: {specific_date}")



# The weekday() method is used to get the day of the week for the specified date. 
# It returns the day of the week, where Monday is 0 and Sunday is 6.
from datetime import datetime

now = datetime.now()
day_of_week = now.weekday()

print(f"\n.weekday(): {day_of_week}")



