#!/usr/bin/env python3

import sys
import datetime
import calendar


def find_weekday(date):
    weekday = (datetime.datetime(date[0], date[1], date[2]).weekday() + 1) % 7
    return str(weekday)

def is_date(string):
    try:
        if len(string) != 9:
            return False
        int(string)
        year = int(string[0:4])
        month = int(string[4:6])
        day = int(string[6:8])
        datetime.datetime(year, month, day)
        if find_weekday([year, month, day]) != string[8]:
            return False
        return True
    except:
        return False

def parse_date(date, format="%Y %m%d %w"):
    week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    year = date[0:4]+""
    month = date[4:6]+"-"
    day = date[6:8]+""
    format_symbol = ["%Y", "%m", "%d", "%w"]
    weekday = "星期"+week_day[int(date[8])]
    format_content = [year, month, day, weekday]
    date = format
    for i in format_symbol:
        date = date.replace(i, format_content[format_symbol.index(i)])
    return date

if __name__ == "__main__":
    argvs = sys.argv
    argvs = argvs[1:]
    if len(argvs) == 1:
        if len(argvs[0]) == 8:
            argvs[0] += find_weekday([int(argvs[0][0:4]), int(argvs[0][4:6]), int(argvs[0][6:8])])
        if not is_date(argvs[0]):
            print("Not Date!")
            exit()
        elif is_date(argvs[0]):
            print(argvs[0])
            exit()
    if len(argvs) == 2:
        print(parse_date(argvs[0], argvs[1]))
