# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k ==0:
            return head
        curr = head
        lenght = 1
        while curr.next:
            lenght += 1
            curr = curr.next
        k =  k % lenght
        if k == 0:
            return head
        curr.next = head

        steps =lenght - k
        tail = head
        for _ in range(steps - 1):
            tail = tail.next

   
        newhead = tail.next 
        tail.next = None
        return newhead
        
        