#!/usr/bin/python3

def simple_delete(a_dict, key):
    try:
        a_dict.pop(key)
    except:
        pass
    return a_dict
