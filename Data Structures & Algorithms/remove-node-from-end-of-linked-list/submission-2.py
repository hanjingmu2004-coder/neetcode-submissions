# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,j=1,head
        while j.next:
            l+=1
            j=j.next 
        if n==l:
            return head.next
        else:
            dummy,cur,i=head,head,1
            while i<l-n:
                cur=cur.next
                i+=1
            cur.next=cur.next.next
        return dummy