# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less=ListNode(-1)
        dummy_great=ListNode(-1)
        less=dummy_less
        great=dummy_great
        curr=head
        while curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                great.next=curr
                great=great.next
            curr=curr.next
        great.next=None
        less.next=dummy_great.next
        return dummy_less.next
