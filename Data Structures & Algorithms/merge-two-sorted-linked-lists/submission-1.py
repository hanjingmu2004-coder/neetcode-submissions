# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val<=list2.val:
            curr=list1
            temp=list2
        else:
            curr=list2
            temp=list1
        prev=ListNode()
        prev.next=curr
        while curr:
            if not curr.next:
                curr.next=temp
                break
            if curr.next.val<=temp.val:
                curr=curr.next
            else:
                tmp=curr.next
                curr.next=temp
                temp=tmp
        return prev.next