#  In Python, you can convert a datetime object to a timestamp and vice versa. Converting datetime to timestamp
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

print(f".timestamp(): {timestamp}") 



#  Converting a timestamp to a datetime object
from datetime import datetime

timestamp = 4650650506
dt_object = datetime.fromtimestamp(timestamp)

print(f"\n.fromtimestamp(): {dt_object}")



# Parsing a date from a string
from datetime import