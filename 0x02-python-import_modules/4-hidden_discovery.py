#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import hidden_4

names = dir(hidden_4)

for name in names:
    if (name[0] != '_'):
        print(name)
