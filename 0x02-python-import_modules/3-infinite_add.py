#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import sys

sum = 0
for index, value in enumerate(sys.argv):
    if index == 0:
        continue

    sum = sum + int(value)
print(sum)
