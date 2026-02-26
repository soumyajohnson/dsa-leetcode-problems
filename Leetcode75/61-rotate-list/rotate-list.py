# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        k=k%l
        if k==0 or l==1:
            return head
        dummy=ListNode(-1,head)
        while k>0:
            first=prev=dummy.next
            end=first.next
            while end.next:
                end=end.next
                prev=prev.next
            end.next=first
            first=end
            prev.next=None
            dummy.next=first
            k-=1
        return dummy.next
            