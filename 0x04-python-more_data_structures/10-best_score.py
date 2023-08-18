#!/usr/bin/python3

def best_score(a_dict):
    try:
        return list(a_dict.keys())[list(a_dict.values()).index(max(a_dict.values()))]
    except:
        return None
