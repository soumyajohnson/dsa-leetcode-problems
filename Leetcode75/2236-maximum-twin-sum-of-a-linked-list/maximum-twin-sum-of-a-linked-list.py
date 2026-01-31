# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev=head
        curr=head.next
        maxsum=0
        while curr and curr.next:
            prev=prev.next
            curr=curr.next.next
        curr=prev.next
        prev.next=None
        first=None
        while curr:
            tmp=curr.next
            curr.next=first
            first=curr
            curr=tmp
        while first:
            v1=first.val
            v2=head.val
            maxsum=max(v1+v2, maxsum)
            first=first.next
            head=head.next
        return maxsum

