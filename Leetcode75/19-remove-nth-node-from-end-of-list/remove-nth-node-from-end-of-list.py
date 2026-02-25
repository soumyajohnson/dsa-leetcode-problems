# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            curr=curr.next
            l+=1
        n=l-n
        dummy=ListNode(0,head)
        prev=dummy
        while n>0:
            prev=prev.next
            n-=1
        prev.next=prev.next.next
        return dummy.next
        