#!/usr/bin/python3

def multiply_by_2(a_dict):
    new_dict = {}
    for i in a_dict.keys():
        new_dict[i] = a_dict[i] * 2
    return new_dict
