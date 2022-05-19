question = '''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.

All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def feb_days(year: int):
    if year % 400 == 0:
        return 29
    if year % 100 == 0:
        return 28
    if year % 4 == 0:
        return 29
    return 28


def solution():
    first_suns = 0
    start = 0
    for year in range(1900, 2001):
        for month in range(12):
            if start == 6 and year > 1900:
                first_suns += 1
            if month == 1:
                days = feb_days(year)
            else:
                days = month_days[month]
            start = (start + days) % 7

    print(first_suns)
