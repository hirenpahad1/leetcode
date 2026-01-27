# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head or k == 0:
            return head
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        tail.next = head

        steps = length - k
        curr = head

        for _ in range(steps-1):
            curr = curr.next
        newhead = curr.next
        curr.next = None
        return newhead
        