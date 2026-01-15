#!/usr/bin/python3
def fizzbuzz(n):

    for n in range (101):
        if n % 3 == 0 and n % 5 == 0:
            print("Fizz Buzz", end=" ")
        elif n % 3 == 0:
            print('Fizz', end=" ")
        elif n % 5 == 0:
            print('Buzz', end=" ")
        else:
            print(n, end=" ")
