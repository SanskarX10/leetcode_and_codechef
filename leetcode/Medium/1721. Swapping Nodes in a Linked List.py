"""

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = head
        for i in range(1, k):
            first = first.next

        null_checker = first 
        while null_checker.next:
            last = last.next
            null_checker = null_checker.next
        first.val, last.val = last.val, first.val
        return head
        
