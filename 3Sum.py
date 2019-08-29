#!/usr/bin/env python3
# encoding: utf-8

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        solutions = set()
        nums = sorted(nums)
        for i in range(0, n-2):
            a = nums[i]
            front = i + 1
            back = n - 1
            while front < back:
                b = nums[front]
                c = nums[back]
                if a+b+c == 0:
                    sol = (a, b, c)
                    solutions.add(sol)
                    front += 1
                    back -= 1
                elif a+b+c > 0:
                    back -= 1
                else:
                    front += 1
        ret = []
        for s in solutions:
            r = []
            for e in s:
                r.append(e)
            ret.append(r)
        return ret




def main():
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    s = solution.threeSum(nums)



if __name__ == '__main__':
    main()
