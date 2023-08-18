#!/usr/bin/python3

def print_sorted_dictionary(dict1):
    list1 = list(dict1.keys())
    list1.sort()
    for i in list1:
        print("{}: {}".format(i, dict1[i]))
