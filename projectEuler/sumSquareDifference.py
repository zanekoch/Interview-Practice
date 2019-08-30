#!/usr/bin/env python3
# encoding: utf-8
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''



def main():
    sum = 0
    square_sum = 0
    for i in range(101):
        sum += i
        square_sum += i * i

    sum = sum * sum
    return sum - square_sum




if __name__ == '__main__':
    main()
