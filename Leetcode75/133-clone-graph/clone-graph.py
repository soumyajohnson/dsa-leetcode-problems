"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map=defaultdict()
        if not node:
            return None
        clone_map[node]=Node(node.val)
        q=deque([node])
        while q:
            curr=q.popleft()
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei]=Node(nei.val)
                    q.append(nei)
                clone_map[curr].neighbors.append(clone_map[nei])
        return clone_map[node]