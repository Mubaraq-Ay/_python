from datetime import date, datetime

now = datetime.now()
print(now)

day = now.day
print(day)

month = now.month
print(month)

year = now.year
print(year)

minute = now.minute
print(minute)

timestamp = now.timestamp()
print(timestamp)

# format the current date.

current_date = now.strftime('%m/%d/%Y, %H:%M:%S')
print(current_date)

# change string to time.
today_date_string = '5 December, 2019'

time_obj = datetime.strptime(today_date_string, '%d %B, %Y')
print(time_obj)

today = datetime(year=2026, month=8, day=7, hour=18, minute=47, second=33)
next_year = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
time_diff = next_year - today
print(time_diff)

today = datetime(year=2026, month=8, day=7, hour=18, minute=47, second=33)
unix_year = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
time_diff = today - unix_year
print(time_diff)


'''keep track of time
- User login timestamps
- Blog post timestamps
- Countdown timers
- Calculating age
- Exam countdown
- Scheduling reminders
- Logging application events
- File creation and modification times
- to get the time the post was uploaded.'''