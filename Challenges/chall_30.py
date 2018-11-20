#!/usr/local/bin/python3
# Python Challenge - 30
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
# Username: repeat; Password: switch
# Keyword:


def main():
    '''
    Hint: relax you are on 30; picture of beach scene
    The picture is only meant to help you relax
    while you look at the csv file
    '''
    with open('./relax_chall_30/yankeedoodle.csv') as csvfile:
        nums = [n.strip() for n in csvfile.read().split(',')]
        total_nums = len(nums)  # 7367

    return 0


if __name__ == '__main__':
    main()
