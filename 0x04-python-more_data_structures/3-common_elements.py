#!/usr/bin/python3

def common_elements(set1, set2):
    result = []
    for elem in set1:
        if elem in set2:
            result.append(elem)
    return result
