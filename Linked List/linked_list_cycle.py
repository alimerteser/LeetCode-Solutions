from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s_pointer, f_pointer = head, head.next

        while f_pointer and f_pointer.next:
            if s_pointer == f_pointer:
                return True
            s_pointer = s_pointer.next
            f_pointer = f_pointer.next.next

        return False
