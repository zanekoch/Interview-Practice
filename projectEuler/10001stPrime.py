#!/usr/bin/env python3
# encoding: utf-8
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(num, primes):
    for prime in primes:
        if num % prime == 0:
            return False
    return True


def main():
    count = 6
    num = 13
    primes = [3, 5, 7, 11, 13]
    while count < 10001:
        num += 2
        if isPrime(num, primes):
            count += 1
            primes.append(num)
    print(num)

if __name__ == '__main__':
    main()
