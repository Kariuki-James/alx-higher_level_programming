#!/usr/bin/python3

if __name__ != "__main__":
    quit()

import sys
from calculator_1 import add, sub, mul, div

operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

result = operators[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
