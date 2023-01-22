'''
Estimated time
20-30 minutes

Level of difficulty
Medium

Prerequisites
LAB 4.3.1.6
LAB 4.3.1.7

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
building a set of utility functions;
utilizing the student's own functions.
Scenario
Your task is to write and test a function which takes three arguments
(a year, a month, and a day of the month) and returns the corresponding day of the year
, or returns None if any of the arguments is invalid.

Use the previously written and tested functions. Add some test cases to the code.
This test is only a beginning.

def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))

'''

# solution 

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    elif month == 2 and is_year_leap(year):
        return 29
    else:
        return months[month-1]

    
def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None
    if month == 2 and is_year_leap(year) and day > 29:
        return None
    if day > days_in_month(year, month):
        return None
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    days += day
    if is_year_leap(year) and month > 2:
        days+=1
    return days

print(day_of_year(2000, 12, 31))
