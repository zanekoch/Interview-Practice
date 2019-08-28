#!/usr/bin/env python3
# encoding: utf-8
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        shift = 1
        result = 0
        while l1 != None or l2 != None:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            result += (val1 + val2) * shift
            shift *= 10
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        li = []
        for i in range(len(str(result))):
            node = ListNode(str(result)[i])
            li.insert(0, node)
        for i in range(len(li) - 1):
            li[i].next = li[i+1]
        return li[0]


def main():
    lOne_1 = ListNode(3)
    lOne_2 = ListNode(4)
    lOne_3 = ListNode(2)
    lOne_2.next = lOne_1
    lOne_3.next = lOne_2

    lTwo_1 = ListNode(4)
    lTwo_2 = ListNode(6)
    lTwo_3 = ListNode(5)
    lTwo_2.next = lTwo_1
    lTwo_3.next = lTwo_2

    solver = Solution()

    solution_node = solver.addTwoNumbers(lOne_3,lTwo_3)

    
if __name__ == '__main__':
    main()
