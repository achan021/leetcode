'''
Leetcode:
Date : 13/5/2022
Title : Squares of a Sorted Array
Difficulty : Easy
Description :
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''

#Solution 1
#Split +ve and -ve list, reverse the order for -ve list when adding
#Perform merge sort
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive_list = []
        negative_list = []
        for val in nums:
            if val < 0:
                negative_list.insert(0,val**2)
            else:
                positive_list.append(val**2)
        return_list = []
        p_cur = 0
        n_cur = 0
        
        while p_cur < len(positive_list) and n_cur < len(negative_list):
            if positive_list[p_cur] < negative_list[n_cur]:
                return_list.append(positive_list[p_cur])
                p_cur += 1
            elif positive_list[p_cur] > negative_list[n_cur]:
                return_list.append(negative_list[n_cur])
                n_cur += 1
            elif positive_list[p_cur] == negative_list[n_cur]:
                return_list.append(positive_list[p_cur])
                p_cur += 1
                return_list.append(negative_list[n_cur])
                n_cur += 1
                
        if p_cur < len(positive_list):
            return_list += positive_list[p_cur:]
        elif n_cur < len(negative_list):
            return_list += negative_list[n_cur:]
        
        return return_list

#Solution 2
#Similar to my implementation but it uses 2 pointer on the main list.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return return_array
