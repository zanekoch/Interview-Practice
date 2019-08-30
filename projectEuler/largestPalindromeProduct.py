#!/usr/bin/env python3
# encoding: utf-8
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
    num = str(num)
    front = 0
    end = len(num) - 1
    while front < end:
        if num[front] != num[end]:
            return False
        front += 1
        end -= 1
    return True

def muliplier():
    ans = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if isPalindrome(i*j) and i*j > ans:
                ans = i*j
    return ans 

def main():
    print(muliplier())




if __name__ == '__main__':
    main()
