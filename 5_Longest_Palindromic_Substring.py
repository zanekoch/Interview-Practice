#!/usr/bin/env python3
# encoding: utf-8
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    #probably should be recursive
    #idea: the longest palindromic substring is the longest palindromic substring betweeen: first half, second half, and spanning the halves
    #=> divide and conquer where you check for palidrome when recombining
    #divide and conquer is too slow so => dynamic programming
    #DP recurrence: M(i,j) = True if M[i+1:j-1] is True and s[i]==s[j] else False
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        answer = ''
        max_length = 0
        m = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            m[i][i] = True
            max_length = 1
            answer = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                m[i][i+1] = True
                answer = s[i:i+2]
                max_len = 2
        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and m[i+1][j-1] == True:
                    m[i][j] = True
                    if max_length < j - i + 1:
                        answer = s[i:j+1]
                        max_length = j - i + 1
        return answer


def main():
    solution = Solution()
    print(solution.longestPalindrome('cbbd'))
if __name__ == '__main__':
    main()
