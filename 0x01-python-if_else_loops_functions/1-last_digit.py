#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = int(str(number)[-1])
else:
    last_num = -int(str(number)[-1])
str1 = "Last digit of " + str(number) + " is " + str(last_num) + " and is "
if last_num>5:
    print(str1 + "greater than 5")
elif last_num == 0:
    print(str1 + "0")
else:
    print(str1 + "less than 6 and not 0")
