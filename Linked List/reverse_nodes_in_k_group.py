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
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            tail = prev
            for i in range(k): #get kth node
                tail = tail.next
                if not tail:
                    return dummy.next  # return if remaining elements are less than k

            next_group = tail.next
            tail.next = None

            # reverse the group
            rev_head = self.reverseList(prev.next)

            # link the reversed group
            tmp = prev.next
            prev.next = rev_head
            tmp.next = next_group
            prev = tmp