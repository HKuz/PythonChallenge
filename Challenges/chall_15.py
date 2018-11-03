#!/usr/local/bin/python3
# Python Challenge - 15
# http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html
# Username: huge; Password: file
# Keyword: mozart

import calendar


def main():
    '''
    Hint: whom? he ain't the youngest, he is the second
    todo: buy flowers for tomorrow
    January 26th (a Monday) is circled on a calendar
    Year shows 1XX6 and is a leap year
    '''
    valid_years = []
    for y in range(1006, 1996, 10):
        # Check if leap year and January 26th was a Monday (0)
        if calendar.isleap(y) and calendar.weekday(y, 1, 26) == 0:
            # print(y)
            valid_years.append(y)

    print(valid_years)  # [1176, 1356, 1576, 1756, 1976], Not youngest so 1756
    # Mozart born on January 27, 1756

    return 0


if __name__ == '__main__':
    main()
