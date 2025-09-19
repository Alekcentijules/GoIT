# The time.time() method returns the current time in seconds since 1 January 1970 (epoch time).
import time

current_time = time.time()
print(f"current_time: {current_time}")



# The time.sleep(seconds) method stops the execution of the program for the specified number of seconds. 
# For example, this code stops the program for 5 seconds.
import time

print("\nStart of pause!")
time.sleep(0)
print("End of pause!")



# The time.ctime([seconds]) method converts the time stamp (number of seconds) into a human-readable text representation. 
# If the argument is not specified, the current time is used.The time.ctime([seconds]) method converts the time stamp 
# (number of seconds) into a human-readable text representation. If the argument is not specified, the current time is used.
import time

current_time = time.time()
print(f"\ncurrent_time: {current_time}")

readable_time = time.ctime(current_time)
print(f"readable_time: {readable_time}")



# The time.localtime([seconds]) method converts the timestamp to the struct_time structure in the local time zone.
# If the argument is not specified, the current time is used.The time.ctime([seconds]) method converts the time stamp 
# (number of seconds) into a human-readable text representation. If the argument is not specified, the current time is used.
import time

current_time = time.time()
print(f"\ncurrent_time: {current_time}")# If the argument is not specified, the current time is used.The time.ctime([seconds]) method converts the time stamp 
# (number of seconds) into a human-readable text representation. If the argument is not specified, the current time is used.
import time

current_time = time.time()
print(f"\ncurrent_time: {current_time}")

local_time = time.localtime(current_time)
print(f"local_time: {local_time}")



# The method time.gmtime([seconds]) is similar to localtime, but turns struct_time to UTC.
import time

current_time = time.time()
utc_time = time.gmtime(current_time)

print(f"\nutc_time: {utc_time}")



# Quite important is the time.perf_counter() method, which provides access to a high-precision counter and is ideal 
# for measuring short time intervals.
# This counter has the highest accuracy available for measuring short time periods and is used primarily to determine 
# the time of code execution.
# How does it work? The time.perf_counter() method returns a value in seconds (as a real number) from some point, for example, 
# from the moment the program starts, and this value increases monotonically. This means that it can be used to accurately 
# measure time intervals.
# Let's use time.perf_counter() to measure the execution time of a certain block of code:
import time

star_time = time.perf_counter()

for _ in range(1_000_000):
    pass

end_time = time.perf_counter()
execution_time = end_time - star_time
print(f"\nexecution_time: {execution_time} sec")



