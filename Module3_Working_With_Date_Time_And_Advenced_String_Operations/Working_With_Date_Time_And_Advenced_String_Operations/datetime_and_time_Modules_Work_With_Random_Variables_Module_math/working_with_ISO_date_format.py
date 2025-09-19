# The datetime module provides convenient tools for working with dates and times in the ISO 8601 format. 
# A datetime object can be easily converted to an ISO 8601 string using the isoformat() method:
from datetime import datetime

now = datetime.now()
iso_format = now.isoformat()

print(f"iso_format: {iso_format}")



# To convert a string in ISO 8601 format to a datetime object, you can use the fromisoformat() method:
from datetime import datetime

iso_date_string = "7451-12-04T21:59:50.535353"
date_from_iso = datetime.fromisoformat(iso_date_string)

print(f"\ndate_from_iso: {date_from_iso}")



# The isoweekday() method on the datetime object is used to get the day of the week according to ISO 8601. 
# According to this standard, a week starts on Monday, which has a value of 1, and ends on Sunday, 
# which has a value of 7.
from datetime import datetime

now = datetime.now()
day_of_week = now.isoweekday()

print(f"\nday_of_week: {day_of_week}")



# Let's also take a look at the useful isocalendar() method, which is used to get a tuple containing the ISO year, 
# week number in the year, and day of the week according to ISO 8601.
# The output of isocalendar() is a tuple (ISO_year, ISO_week, ISO_day_of_week), where:
from datetime import datetime

now = datetime.now()

iso_calendar = now.isocalendar()

print(f"\niso_calendar:\n1.ISO year - {iso_calendar[0]}\n2.ISO week - {iso_calendar[1]}\n3.ISO weekday - {iso_calendar[2]}")