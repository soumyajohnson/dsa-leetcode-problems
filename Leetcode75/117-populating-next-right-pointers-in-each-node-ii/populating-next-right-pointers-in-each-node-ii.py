"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q=deque([root])
        dummy=Node(-999)
        while q:
            l=len(q)
            prev=dummy
            for _ in range(l):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    prev.next=node.left
                    prev=prev.next
                if node.right:
                    q.append(node.right)
                    prev.next=node.right
                    prev=prev.next
        return root