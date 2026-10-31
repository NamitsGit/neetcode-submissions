# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # finding the mid-point
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        # reverse the second part
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            f_next, s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next
        





