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

min = now.minute
print(min)

sec = now.second
print(sec)

timestamp = now.timestamp()
print(timestamp) 

# timestamp or unix timestamp is the number of seconds elapsed since jan 1, 1970.

print(f'{day}/{month}/{year}, {hour}:{min}')