'''
Leetcode:
Date : 7/5/2022
Title : Merge 2 sorted lists
Difficulty : Easy
Description :

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

#Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        head1 = list1
        head2 = list2
        new_ll = None
        new_ll_head = None
        while (head2 != None) and (head1 != None) :
            if head1.val >= head2.val:
                if new_ll == None:
                    new_ll = head2
                    
                else:
                    new_ll.next = head2
                    new_ll = new_ll.next
                head2 = head2.next
            else:
                if new_ll == None:
                    new_ll = head1
                else:
                    new_ll.next = head1
                    new_ll = new_ll.next
                head1 = head1.next
            
            if new_ll_head == None:
                new_ll_head = new_ll
                
        if head2 != None:
            new_ll.next = head2
        elif head1 != None:
            new_ll.next = head1
            
        return new_ll_head

#Solution 2
class Solution:
    def mergeTwoLists(self, a, b):
        #Only recurse if both linked list is not empty
        if a and b:
            #always make sure the smaller node is in the front
            if a.val > b.val:
                a, b = b, a
            #only need to swap out the smaller node
            a.next = self.mergeTwoLists(a.next, b) 
        #top layer return will return head of Linked list
        #end layer return will return the remainder of the 2 or None
        return a or b 
