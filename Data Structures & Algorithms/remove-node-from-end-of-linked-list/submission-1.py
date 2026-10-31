# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur, target = head, head
        target_prev = None
        i = 0
        count = 0
        while cur:
            print(f"{target.val=}")
            if n - i - 1 < 0:
                target_prev = target
                target = target.next
            count += 1
            i += 1
            cur = cur.next
        if n == count:
            return head.next
        target_prev.next = target.next
        return head

        

        
