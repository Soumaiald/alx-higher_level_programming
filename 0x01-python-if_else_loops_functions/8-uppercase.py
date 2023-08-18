#!/usr/bin/python3
def uppercase(val):
    res = list(val)
    for i in range(len(res)):
        if ord(res[i]) in range(97, 123):
            res[i] = chr(ord(res[i]) - 32)
    print("{}".format(''.join(res)))
