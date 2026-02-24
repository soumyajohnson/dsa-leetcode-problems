# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        carry=0
        c1=l1
        c2=l2
        curr=dummy
        while c1 or c2 or carry!=0:
            val1=c1.val if c1 else 0
            val2=c2.val if c2 else 0
            res=(val1+val2+carry)%10
            carry=(val1+val2+carry)//10
            node=ListNode(res)
            curr.next=node
            curr=curr.next
            c1=c1.next if c1 else None
            c2=c2.next if c2 else None
        sumlist=dummy.next
        return sumlist
        