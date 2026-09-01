# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,quick=head,head
        while quick and quick.next:
            slow=slow.next
            quick=quick.next.next
            if slow==quick:
                return True
        return False
        