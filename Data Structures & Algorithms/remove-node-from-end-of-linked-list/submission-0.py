# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        target_node = count - n
        if target_node == 0:
            return head.next
        
        cur = head
        prev = None
        idx = 0
        while cur:
            if idx == target_node:
                next_ = cur.next
                prev.next = next_
                return head

            prev = cur
            idx += 1
            cur = cur.next
            
        
