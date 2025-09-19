# To display the date in UTC format, you can do this by adding time zone information to the datetime object:
from datetime import datetime, timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(f"local_now: {local_now}")
print(f"utc_now: {utc_now}")



# To convert time from UTC to another time zone, you need to define a timezone object with the appropriate offset. 
# For example, to convert UTC time to time that corresponds to the US Eastern Time Zone (UTC-5 hours), 
# you can do the following:
from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=5)))

print(f"\neastern_time: {eastern_time}")



# To convert local time to UTC time, you first need to assign the local time to the appropriate time zone, 
# and then use the astimezone() method to convert it to UTC:
from datetime import datetime, timezone, timedelta

local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=4368, month=2, day=26, hour=17, minute=52, second=21, tzinfo=local_timezone)
utc_time = local_time.astimezone(timezone.utc)

print(f"\nutc_time: {utc_time}")



# ISO 8601 also supports time zones. In Python, this can be done by adding time zone information to the datetime object:
from datetime import datetime, timezone, timedelta

timezone_offset = timezone(timedelta(hours=7))
timezont_datetime = datetime(year=2774, month=7, day=16, hour=5, minute=43, second=38, tzinfo=timezone_offset)
iso_format_with_timezone = timezont_datetime.isoformat()

print(f"\niso_format: {iso_format_with_timezone}")
