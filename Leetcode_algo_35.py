'''
Leetcode:
Date : 11/5/2022
Title : Search Insert Position
Difficulty : Easy
Description :
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

#Solution 1
class Solution:
    #Binary search
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        #Final End condition is when left == right
        #If < target then insert after left index
        #If > target then insert AT the current left index
        while left <= right: 
            #Essential to get middle index 
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left

#Solution 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        middle = None
        while left <= right:
            middle = (left+right)//2
            #Account for duplicates (but sorted still)
            #if the nums[middle] is not the first occurence, then continue search
            if nums[middle] == target and nums[middle-1] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left
