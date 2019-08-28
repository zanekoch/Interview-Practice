#!/usr/bin/env python3
# encoding: utf-8
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''



class Solution:
    #idea is to use divide and conquer so on each recursive call only take half of each array
    #how to determine which half of array to take?
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        mid1 = int(len(nums1)/2)
        mid2 = int(len(nums2)/2)
        print(nums1, nums2, mid1, mid2)
        if len(nums1) <= 2 and len(nums2) <= 2:
            if nums1[0] == nums2[0]:
                return nums1[0]
            else:
                return float((nums1[0]+nums2[0])/2)
        elif nums1[mid1] > nums2[mid2]:
            return self.findMedianSortedArrays(nums1[:mid1], nums2[mid2:])
        else:
            return self.findMedianSortedArrays(nums1[mid1:], nums2[:mid2])

def main():
    nums1 = [1,3]
    nums2 = [2]
    solution = Solution()
    solution.findMedianSortedArrays(nums1, nums2)

if __name__ == '__main__':
    main()
