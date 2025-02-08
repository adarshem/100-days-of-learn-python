from datetime import datetime, timedelta, timezone
import time

# is an external library that provides powerful extensions to the standard datetime module, including support for timezones through the tz module.
# from dateutil import tz

# pytz is an external library that provides support for accurate and cross-platform timezone calculations. It allows you to work with timezones in Python and convert between different timezones.
# import pytz 

# Get the current date and time
now = datetime.now()
print("Current date and time:", now)

# Get the current date
today = now.date()
print("Current date:", today)

# Get the current time
current_time = now.time()
print("Current time:", current_time)


# Format the date and time
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date_time)

# Format the date
formatted_date = now.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

# Format the time
formatted_time = now.strftime("%H:%M:%S")
print("Formatted time:", formatted_time)


# Parse a date and time string
date_time_str = "2023-10-10 14:30:00"
parsed_date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date_time)

# Parse a date string
date_str = "2023-10-10"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)

# Parse a time string
time_str = "14:30:00"
parsed_time = datetime.strptime(time_str, "%H:%M:%S").time()
print("Parsed time:", parsed_time)


# Get the local time
local_time = time.localtime()
formatted_local_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Local time:", formatted_local_time)


# Get the UTC time
utc_time = time.gmtime()
formatted_utc_time = time.strftime("%Y-%m-%d %H:%M:%S", utc_time)
print("UTC time:", formatted_utc_time)


# Calculate a time difference
one_day = timedelta(days=1)
yesterday = now - one_day
tomorrow = now + one_day

print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)

# Calculate the difference between two dates
date1 = datetime(2023, 10, 10)
date2 = datetime(2023, 10, 15)
difference = date2 - date1
print("Difference between dates:", difference)


# Get the current date and time in UTC
now_utc = datetime.now(timezone.utc)
print("Current date and time in UTC:", now_utc)

# Define a timezone offset (e.g., New York is UTC-5 or UTC-4 depending on daylight saving time)
ny_offset = timedelta(hours=-5)
ny_timezone = timezone(ny_offset)

# Get the current date and time in the New York timezone
now_ny = now_utc.astimezone(ny_timezone)
print("Current date and time in New York:", now_ny)

# Define another timezone offset (e.g., Kolkata is UTC+5:30)
kolkata_offset = timedelta(hours=5, minutes=30)
kolkata_timezone = timezone(kolkata_offset)

# Get the current date and time in the Kolkata timezone
now_kolkata = now_utc.astimezone(kolkata_timezone)
print("Current date and time in Kolkata:", now_kolkata)

#---------- how to calculate the difference between two datetime objects ----------#
# Define two datetime objects
datetime1 = datetime(2023, 10, 10, 14, 30, 0)  # October 10, 2023, 14:30:00
datetime2 = datetime(2023, 10, 15, 18, 45, 0)  # October 15, 2023, 18:45:00

# Calculate the difference between the two datetime objects
difference = datetime2 - datetime1

# Print the difference
print("Difference between datetime1 and datetime2:", difference)

# Access the difference in days, seconds, and microseconds
print("Days:", difference.days)
print("Seconds:", difference.seconds)
print("Microseconds:", difference.microseconds)

# Calculate the total difference in seconds
total_seconds = difference.total_seconds()
print("Total difference in seconds:", total_seconds)
total_minutes = difference.total_seconds() / 60
print("Total difference in minutes:", total_minutes)
total_hours = difference.total_seconds() / 3600
print("Total difference in hours:", total_hours)


# # Get the current date and time in UTC
# utc_now = datetime.now(tz=tz.UTC)
# print("Current date and time in UTC:", utc_now)

# # Convert UTC time to local time
# local_timezone = tz.gettz("America/New_York")
# local_time = utc_now.astimezone(local_timezone)
# print("Current date and time in New York:", local_time)

# # Convert local time to another timezone
# another_timezone = tz.gettz("Asia/Kolkata")
# another_time = local_time.astimezone(another_timezone)
# print("Current date and time in Kolkata:", another_time)


# # Get the current date and time in UTC
# utc_now = datetime.now(pytz.utc)
# print("Current date and time in UTC:", utc_now)

# # Convert UTC time to local time
# local_timezone = pytz.timezone("America/New_York")
# local_time = utc_now.astimezone(local_timezone)
# print("Current date and time in New York:", local_time)

# # Convert local time to another timezone
# another_timezone = pytz.timezone("Asia/Kolkata")
# another_time = local_time.astimezone(another_timezone)
# print("Current date and time in Kolkata:", another_time)