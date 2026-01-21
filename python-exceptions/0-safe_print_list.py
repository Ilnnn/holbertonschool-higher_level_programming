#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    fnlcount = 0

    for i in range(x):
        try:
            print(my_list[i], end= "")
            fnlcount += 1
        except IndexError:
            break
    print()
    return fnlcount
