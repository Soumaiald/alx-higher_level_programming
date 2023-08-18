#!/usr/bin/python3

def best_score(a_dict):
    try:
        res = list(a_dict.keys())[list(a_dict.values()).index(max(a_dict.values()))]
    except:
        res =  None
    return res
