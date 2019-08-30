#!/usr/bin/env python3
# encoding: utf-8

from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        output = []
        for list in lists:
            while
                heappush(heap, list.val)
        while heap != []:
            output.append(heappop(heap))
main():
    solution = Solution()
    print(solution.mergeKLists(li))

if __name__ == '__main__':
    main()
