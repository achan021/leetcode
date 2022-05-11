'''
Leetcode:
Date : 11/5/2022
Title : Implement strStr()
Difficulty : Easy
Description :
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

#Solution 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_len = len(needle)
        window_pointer = 0
        if len(haystack) < window_len:
            return -1
        #Note that array slicing is O(m) for m is the len of the slicing
        #BUT m << N for N is the length of the array. Therefore, ultimately
        #O(m*N) is approx O(N)
        while window_pointer + window_len <= len(haystack):
            if haystack[window_pointer : window_pointer + window_len] == needle:
                return window_pointer
            else:
                window_pointer += 1
        return -1

#Solution 2
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Similar to solution 1 but less declarations.
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
