#!/usr/bin/python3

if __name__ != "__main__":
    quit()

import sys

args = len(sys.argv) - 1
print(f"{args} argument", end='')
if args == 0:
    print("s.")
elif args == 1:
    print(":")
else:
    print("s:")

if args > 0:
    for index, value in enumerate(sys.argv):
        if index == 0:
            continue
        print(f"{index}: {value}")
