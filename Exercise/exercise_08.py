"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse


def compute(**kwargs):
    if kwargs.get('action') == "sum":
        sum_input = sum(kwargs.get('input'))
        if kwargs.get('return_float'):
            return float(sum_input)
        else:
            return sum_input
    elif kwargs.get('action') == "mean":
        mean_input = sum(kwargs.get('input')) / len(kwargs.get('input'))
        if kwargs.get('return_float'):
            return float(mean_input)
        else:
            return mean_input


if __name__ == '__main__':
    print(compute(input=[1, 2, 3], action="mean", return_float=False))

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--multiply', help='', type=int)
    parser.add_argument('-s', '--sum', help='', action='store_true')
    parser.add_argument('remainder', help='', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
        if args.sum:
            print('Sum:', sum([int(i) for i in args.remainder]))
        else:
            print('Product:', [int(args.multiply) * int(x) for x in args.remainder])
    except:
        parser.print_help()
        sys.exit(1)
