from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second, first = head, head

        k = 0
        while k < n and first.next:
            first = first.next
            k += 1

        while first.next:
            second = second.next
            first = first.next

        if k == n - 1:
            head = head.next
            return head

        second.next = second.next.next
        return head