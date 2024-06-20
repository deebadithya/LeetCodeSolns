"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""



# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)

        head = seek

        while seek and target:

            while seek.next and seek.next.val < target.val:
                seek = seek.next
            
            seek.next, target = target, seek.next

            seek = seek.next

        return head

        