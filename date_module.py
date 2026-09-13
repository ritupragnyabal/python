# datetime
from datetime import datetime
current_time_zone = datetime.now()
print(current_time_zone)  # Output: current date and time in the format YYYY-MM-DD HH:MM:SS.mmmmmm

# get individual components of the date and time

print(current_time_zone.year)
print(current_time_zone.month)
print(current_time_zone.day)
print(current_time_zone.hour)
print(current_time_zone.minute)
print(current_time_zone.second)

# formatted
info = datetime.now()
formatted =info.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # Output: current date and time in the format YYYY-MM-DD HH

# convert string to date - from spis (recievig data from api or user input)

# date_string = "2023-07-15"
# date = datetime.strptime(
#     date_string, 
#     "%Y-%m-%d"
#     )
# print(date)  # Output: 2023-07-15 00:00:
# print(type(date))  # Output: <class 'datetime.datetime'>

# # timedelta - to perform arithmetic operations on date and time
# from datetime import timedelta
# event_name = "Python wokshop"
# event_date = date(2026, 9, 15)
# # registration deadline is 5 days before the event
# registration_deadline = event_date - timedelta(days=5)
# print("--------------EVENT REGISTRATION----------------")
# name = input("Enter your name: ")
# email = input("Enter your email: ")
# today = date.today()

# print("\nEvent Name:", event_name)
# print("Event Date:", event_date)
# print("Registration Deadline:", registration_deadline)
# print("Today's Date:", today)

# # check if registration is open or closed
# if today <= registration_deadline:
#     print("\nRegistration Successful!")
#     print("Participant Name:", name)
#     print("Participant Email:", email)  
    
#     # calculate days left for registration
#     remaining_days = event_date - today
#     print("Days left for registration:", remaining_days.days)
# else:
#     print("\nRegistration Closed!")
#     print("THE RESISTRATION DEADLINE HAS PASSES")
    
# # CALCULATE DIFFERENCE BETWEEN TWO DATES
# start = datetime(2023, 7, 15)
# end = datetime(2023, 8, 15)
# difference = end - start
# print("Difference between two dates:", difference.days, "days")  # Output: Difference between two dates: 31 days

# # calender module
import calendar
print(calendar.month(2023, 7))  # Output: July 2023 calendar

import calendar
print(calendar.isleap(2020))  # Output: True (2020 is a leap year)

# time
import time
print(time.time())  # Output: current time in seconds since epoch (January 1, 1970)

print(time.localtime())  # Output: current local time in struct_time format


# sleep
print("Start")
time.sleep(5)  # Pause execution for 5 seconds
print("End")


# date & time module
from datetime import datetime, timedelta
order_time = datetime.now()
delivery_time = order_time + timedelta(days=5)
print("Order, order time")
print("Delivery:", delivery_time)
