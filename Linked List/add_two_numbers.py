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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        carry = 0

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            if a + b + carry >= 10:
                summ = a + b - 10 + carry
                carry = 1
            else:
                summ = a + b + carry
                carry = 0

            curr.val = summ

            if (l1 and l1.next) or (l2 and l2.next):
                curr.next = ListNode()
                curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry >= 1:
            curr.next = ListNode(val=carry)

        return l3
