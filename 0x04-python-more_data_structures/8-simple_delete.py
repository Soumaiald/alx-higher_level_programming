#!/usr/bin/python3

def simple_delete(a_dict, key):
    try:
        a_dict.pop(key)
        return a_dict
    except:
        return a_dict
