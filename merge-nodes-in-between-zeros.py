"""
merge-nodes-in-between-zeros.py
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        add_ups = 0
        result = ListNode(0)
        start = result
        while current != None:
            if current.val:
                add_ups += current.val
            else:
                result.next = ListNode(add_ups)
                result = result.next
                add_ups = 0
            current = current.next
        return start.next
    
# Solution 2 [ Optimized ]

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, add_ups = head, 0
        while current.next:
            if current.next.val:
                add_ups += current.next.val
                current.next = current.next.next
            else:
                current.next.val = add_ups  
                add_ups = 0
                current = current.next       
        return head.next