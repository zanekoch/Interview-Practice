#!/usr/bin/env python3
# encoding: utf-8

'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    #seems like the knapsack packing problem so maybe DP
    #also could be greedy, but I think not bc two variables (height and distance) to take into account
    def maxArea(self, height) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while (l<r):
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
def main():
    solution = Solution()
    a = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(a))


if __name__ == '__main__':
    main()
