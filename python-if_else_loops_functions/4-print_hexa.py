#!/usr/bin/python3
for i in range(0, 99):
    if i != 98:
        print("{:d} = {:x}, ".format(i, i), end="")
    else:
        print("{:d} = {:x}".format(i, i))
