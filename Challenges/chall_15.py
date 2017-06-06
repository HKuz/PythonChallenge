#!/Applications/anaconda/envs/Python3/bin
# Python challenge - 15
# http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html

from datetime import datetime, timedelta
import calendar

def main():
    '''
    Hint: whom? he ain't the youngest, he is the second
    todo: buy flowers for tomorrow
    January 26th is circled on a calendar
    Year is a leap year, maybe ending in 6
    '''
    valid_years = []
    for y in range(1600, 2017, 1):
        # Check if leap year and January 26th was a Monday (0)
        if calendar.isleap(y) and calendar.weekday(y, 1, 26) == 0:
            # print(y)
            valid_years.append(str(y))

    ends_in_six = []
    for year in valid_years:
        if year[-1] == '6':
            ends_in_six.append(year)

    print(ends_in_six) # 1756, 1976
    # Mozart born on January 27, 1756

    return 0

# Keyword: mozart


if __name__ == '__main__':
    main()
