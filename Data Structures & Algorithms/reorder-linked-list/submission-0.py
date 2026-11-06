# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
0123456
0123 |654

0, 6, 1,5,2,4,3

2 4  6 8
2 4  8 6
2 8  6 4
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid  = slow.next
        slow.next = None
        prev = None
        while mid:
            tmp = mid.next
            mid.next= prev
            prev =mid
            mid = tmp
        
        first , second = head , prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2
