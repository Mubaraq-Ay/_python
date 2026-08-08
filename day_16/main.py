# python datetime.

# python has a datetime module that handles date and time.

import datetime
# we use dir to know the available functions in a module.
# print(dir(datetime))

# getting datetime information.
from datetime import datetime
now = datetime.now()
print(now)


day = now.day
print(day)

month = now.month
print(month)

year = now.year
print(year)

hour = now.hour
print(hour)

minute = now.minute
print(minute)

seconds = now.second
print(seconds)

timestamp = now.timestamp()
print(timestamp) 

# timestamp or unix timestamp is the number of seconds elapsed since jan 1, 1970.

print(f'{day}/{month}/{year}, {hour}:{minute}')


# formatting date output using strftime.
from datetime import datetime

new_year = datetime(2020, 1, 1)
print(new_year)

day = new_year.day
print(day)

month = new_year.month
print(month)

year = new_year.year
print(year)

hour = new_year.hour
print(hour)

minute = new_year.minute
print(minute)

seconds = new_year.second
print(seconds)

print(f'{day}/{month}/{year}, {hour}:{minute}')


# using strftime now.
from datetime import datetime

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print('time:', t)

time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print(f'time_one: {time_one}')

time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print(f'time_two: {time_two}')


# string to time using strptime

from datetime import datetime
date_string = '5 December, 2019'
print(f'date_string: {date_string}')

date_object = datetime.strptime(date_string, '%d %B, %Y')
print(f'date_object: {date_object}')

# using date from datetime.
from datetime import date
d = date(2020, 1, 1)
print(d)
print(f'current date: {d.today()}')

# date object of today's date.


today = date.today()
print(f'current year: {today.year}')
print(f'current month: {today.month}')
print(f'current day: {today.day}')

# time objects to represent time.
from datetime import time

a = time()
print(f'a: {a}')

# time(hour, minute, second)
b = time(10, 30, 50)
print(f'b: {b}')

# time(hour, minute, second)
c = time(hour=10, minute=30, second=50)
print(f'c: {c}')

# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200303) # remember micro is 6 digits.
print(f'd: {d}')


"""
    date only stores: 
        Year
        Month
        Day

    datetime stores:
        Year
        Month
        Day
        Hour
        Minute
        Second
        Microsecond

    time represents only clock.
"""

# difference between two points using time date and datetime.

from datetime import date, datetime

today = date(year=2026, month=8, day=7)
new_year = date(year=2027, month=1, day=1)
time_left_for_new_year = new_year - today
print(f'time left for new year: {time_left_for_new_year}')

t1 = datetime(year = 2026, month = 8, day=7, hour=18, minute=22, second=29)
t2 = datetime(year=2027, month=1, day=1, hour=0, second=0)
diff = t2 - t1
print(f'time left for new year is: {diff}')