#!/usr/bin/env python3
# encoding: utf-8
'''
TA Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def isPythagTrip(a, b, c):
    if (a*a + b*b - c*c) == 0:
        return a * b * c
    return False

def calculator():
    for c in range(998,0,-1):
        for b in range(0, i):
            for a


def main():
    print(calculator())

if __name__ == '__main__':
    main()
