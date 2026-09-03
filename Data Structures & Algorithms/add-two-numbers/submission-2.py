# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=l1)
        i=dummy
        j=ListNode(next=l2)
        carry=0
        while i.next and j.next:
            i=i.next
            j=j.next
            x=i.val+j.val+carry
            i.val=x%10
            carry=x//10
        while i.next:
            i=i.next
            x=i.val+carry
            i.val=x%10
            carry=x//10
        while j.next:
            i.next=j.next
            i=j.next
            j=j.next
            x=j.val+carry
            j.val=x%10
            carry=x//10
        if carry:
            i.next=ListNode(carry)
        return dummy.next