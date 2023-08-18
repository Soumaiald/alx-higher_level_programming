#!/usr/bin/python3

def multiply_list_map(my_list, num):
    def mult(n, a = num):
        return n * a
    return list(map(mult, my_list))
