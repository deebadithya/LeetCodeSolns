"""
swap-nodes-in-pairs.py
24. Swap Nodes in Pairs
Solved
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from list2linkedlist import singlyLinkedList
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import *
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not current:return current
        while current.next:
            current.next.val, current.val = current.val, current.next.val
            if not current.next.next:
                break
            current =  current.next.next
        return head
       
soln = Solution()
inp = singlyLinkedList([1,2,3])
result = soln.swapPairs(inp)

while result:
    print(result.val)
    result = result.next

