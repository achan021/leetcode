'''
Leetcode:
Date : 7/5/2022
Title : Valid Parentheses
Difficulty : Easy
Description :
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

#Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ['(','{','[']
        close_list = [')','}',']']
        list_dict = dict(zip(open_list,close_list))
        stack_list = []
        if len(s) == 1:
            return False
        for sym in s:
            if len(stack_list) == 0 and sym in close_list:
                return False
            if sym in list_dict.keys():
                stack_list.append(sym)
            else:
                top_sym = stack_list[-1]
                top_pair_sym = list_dict[top_sym]
                if top_pair_sym != sym:
                    return False
                else:
                    stack_list.pop()
        if len(stack_list) == 0:
            return True
        else:
            return False
