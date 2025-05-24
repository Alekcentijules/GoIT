from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted_date: {formatted_date}")

formatted_date_only = now.strftime("%A, %d %B %Y")
print(f"\nformatted_date_only: {formatted_date_only}")

formatted_time_only = now.strftime("%I:%M %p")
print(f"\nformatted_time_only: {formatted_time_only}")

formatted_date_only = now.strftime("%d.%m.%Y")
print(f"\nformatted_date_only: {formatted_date_only}")



# Let's consider the case when there is a date string "2023.03.14" from a website and we need to convert it 
# to an object before saving the date to the database
from datetime import datetime

date_string = "5375.06.22"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")

print(f"\ndatetime_object: {datetime_object}")