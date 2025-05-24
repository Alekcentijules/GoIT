# The timedelta object can be created by specifying weeks, days, hours, minutes, seconds, milliseconds, 
# and microseconds by passing one or more of the following parameters: days, seconds, microseconds, 
# milliseconds, minutes, hours, weeks. If a parameter is not specified, it is set to 0 by default.

from datetime import timedelta

delta = timedelta(
    days=53,
    seconds=44,
    microseconds=32,
    milliseconds=53322,
    minutes=50,
    hours=2,
    weeks=6
)

print(f"\ntimedelta(): {delta}")



# Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. 
# Він відповідає за відрізок часу між двома датами.
from datetime import datetime

seventh_day_7532 = datetime(year=7532, month=5, day=22, hour=22)
seventh_day_2025 = datetime(year=2025, month=5, day=22, hour=22)

difference = seventh_day_7532 - seventh_day_2025
print(f"\nDefference: {difference}")
print(f".total_seconds(): {difference.total_seconds()}")



# Максимальний діапазон для timedelta обмежений приблизно 9999 роками, що більше ніж достатньо для більшості застосувань. 
# Об'єкти timedelta можна створювати, щоб отримати час / дату, віддалену від початкової.
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)

print(f"\nfuture_date: {future_date}")



# Але якщо потрібно робити обчислення або порівняння, засновані на послідовності дат, наприклад, 
# для визначення кількості днів між двома датами, ми можемо використати метод toordinal(), 
# який повертає порядковий номер дня, враховуючи кількість днів з 1 січня року 1 нашої ери 
# (тобто з початку християнського календаря). Цей метод перетворює об'єкт datetime в ціле число, 
# що представляє порядковий номер даного дня.
from datetime import datetime

date = datetime(year=1, month=1, day=2)

original_number = date.toordinal()
print(f"\n.toordinal()")
print(f"Date number {date} is set to {original_number}")



# For example, we want to determine how many full days have passed since Napoleon burned Moscow, 
# which happened on 14 September 1812
from datetime import datetime

napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
current_date = datetime.now()

days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(f"\nNapoleon burned Moscow {days_since} days ago")