from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        s_pointer, f_pointer = head, head.next
        l1 = head

        while f_pointer and f_pointer.next:
            s_pointer = s_pointer.next
            f_pointer = f_pointer.next.next

        if f_pointer is None:  # if f_pointer is None, number of elements is even
            l2 = s_pointer
        else:  # if f_pointer is not None, number of elements is odd
            l2 = s_pointer.next

        l2 = self.reverseList(l2)
        s_pointer.next = None

        while l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l2 = next2
            l1 = next1
