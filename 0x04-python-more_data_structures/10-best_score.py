#!/usr/bin/python3

def best_score(a_dict):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    return list(a_dict.keys())[list(a_dict.values()).index(max(a_dict.values()))]
