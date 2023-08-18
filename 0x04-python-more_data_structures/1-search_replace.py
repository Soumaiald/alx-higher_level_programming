#!/usr/bin/python3

def search_replace(my_list, a, b):
    new_list = []
    for elem in my_list:
        if elem  == a:
            new_list.append(b)
        else:
            new_list.append(elem)
    return new_list
