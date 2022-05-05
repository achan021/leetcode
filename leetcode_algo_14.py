'''
Leetcode:
Date : 6/5/2022
Title : Longest Common Prefix
Difficulty : Easy
Description:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

#Solution 1
class Solution:
    def get_min_len(self,strs):
        min_len = None
        min_word = None
        for word in strs:
            if min_len is None:
                min_len = len(word)
                min_word = word
            else:
                if len(word) < min_len:
                    min_len = len(word)
                    min_word = word
        return min_len,min_word
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            min_len,min_word = self.get_min_len(strs)
            prefix = None
            output_prefix = ""
            for i in range(len(min_word)):
                prefix = min_word[:i+1]
                common_bool = all([True if prefix == word[:i+1] else False for word in strs]) #all() will do logical AND against all values in list. any() will do logical OR
                if common_bool:
                    output_prefix = prefix
                else:
                    break
            return output_prefix

#Solution 2
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
                
        out = ''
        # use an array to and min() to get the len of smallest word
        nmax = min([len(s) for s in strs])
        terminate = False
        for i in range(nmax):
            char = strs[0][i] #reference the first word in the list
            for s in strs[1:]:
                if s[i] != char: 
                    terminate = True
                    break
            if not terminate:
                out += char
                
        return out

#Solution 3
'''
strs = ["flower","flow","flight"]
l = list(zip(*strs))
>>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

#Solution 4
'''
 i      0  1  2  3  4  5
 0      f  l  o  w  e  r
 1	f  l  o  w
 2	f  l  i  g  h  t
		
We choose the first string in the list as a reference. in this case is str[0] = "flower"
the outside for-loop go through each character of the str[0] or "flower". f->l->o->w->e->r
the inside for-loop, go through the words, in this case is flow, flight.


strs[j][i] means the the i's character of the j words in the strs.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0: return ""
        for i in range(len(strs[0])): 
            c = strs[0][i]// 
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0] if strs else ""
