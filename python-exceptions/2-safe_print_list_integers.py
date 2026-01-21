#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    fnlcountdwn = 0

    for i in range(x):
        try:
            try: 
                print("{:d}".format(my_list[i]), end="")
                fnlcountdwn += 1
            except (ValueError, TypeError):
                pass            
        except IndexError:
                break
    print()
    return fnlcountdwn