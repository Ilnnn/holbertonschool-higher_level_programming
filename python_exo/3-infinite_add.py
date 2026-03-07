#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numb = 0

    for arg in sys.argv[1:]:
        numb += int(arg)
    print(numb)