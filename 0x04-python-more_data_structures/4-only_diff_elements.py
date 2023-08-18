#!/usr/bin/python3

def only_diff_elements(set1, set2):
    result = list(set1)
    for elem in set2:
        if elem  in set1:
            result.remove(elem)
        else:
            result.append(elem)
    return result
