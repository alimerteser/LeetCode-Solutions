class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None, None)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None, cur)

    def delete(self, val):
        if not self.head:
            return

        curr = self.head
        while curr and curr.val != val:
            curr = curr.next

        if val == self.head.val:
            self.head = curr.next
            if curr.next:
                curr.next.prev = None

        if curr and curr.prev:
            curr.prev.next = curr.next
        if curr and curr.next:
            curr.next.prev = curr.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.ll = LinkedList()
        self.cache = dict()

    def get(self, key: int) -> int:
        if self.cache.get(key, None) is not None:
            self.ll.delete(key)
            self.ll.append(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) is not None:
            self.ll.delete(key)
            self.ll.append(key)
            self.cache[key] = value
        elif self.size == self.capacity:
            self.cache.pop(self.ll.head.val)
            self.ll.delete(self.ll.head.val)
            self.ll.append(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.ll.append(key)
            self.size += 1
