#!/usr/bin/python3

if __name__ == "__main__":
    """Print sum  of argv"""
    import sys
    count = 0
    for i in range(1, len(sys.argv)):
        count = count + int(sys.argv[i])
    print("{}".format(count))

        
