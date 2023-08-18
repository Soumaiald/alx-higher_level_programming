#!/usr/bin/python3
def search_replace(my_list, a, b):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i]  == a:
            new_list.append(b)
        else:
            new_list.append(my_list[i])
    return new_list
