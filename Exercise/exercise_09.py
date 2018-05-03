"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def time_function(some_func):
    def wrapper():
        t1 = time.time()
        d1 = time.process_time()
        value = some_func()
        t2 = time.time()
        d2 = time.process_time()
        delta = t2 - t1
        delta2 = d2 - d1
        print("Real World Time Taken: " + str(delta))
        print("Process Time Taken(ms): " + str(delta2 * 1000))
        print("Size of Return Value: " + str(sys.getsizeof(value))+"\n")
        return value
    return wrapper


def get_log(some_func):
    def wrapper():
        value = some_func()
        result = [math.log10(x) for x in value]
        return result
    return wrapper


@time_function
@get_log
def for_loop():
    print("for_loop():")
    a = []
    for i in range(1, 1000000):
        a.append(i)
    return a


@time_function
@get_log
def list_comp():
    print("list_comp():")
    a = [i for i in range(1, 1000000)]
    return a


@time_function
@get_log
def numpy_list():
    print("numpy_list():")
    a = numpy.arange(1, 1000000)
    return a


@time_function
@get_log
def pandas_list():
    print("pandas_list():")
    data = numpy.arange(1, 1000000)
    dataframe = pandas.DataFrame(data)
    return dataframe.values


@time_function
@get_log
def generator_list():
    print("generator_list():")
    a = (i for i in range(1, 1000000))
    return a


for_loop()
list_comp()
numpy_list()
pandas_list()
generator_list()
