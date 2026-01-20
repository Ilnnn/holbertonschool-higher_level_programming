#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    al_keys =sorted(a_dictionary.keys())

    for key in al_keys:
        print("{}: {}".format(key, a_dictionary[key]))
