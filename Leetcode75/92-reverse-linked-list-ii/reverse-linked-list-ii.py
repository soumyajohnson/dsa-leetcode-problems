# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        i=1
        curr=dummy
        while i<left:
            i+=1
            curr=curr.next
        before=curr
        first=curr.next
        curr=first
        prev=None
        while i<=right:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
            i+=1
        before.next=prev
        first.next=curr
        return dummy.next
        

