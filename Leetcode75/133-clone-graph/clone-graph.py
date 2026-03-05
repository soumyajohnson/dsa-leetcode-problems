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
        copied={}
        def dfs(node):
            if not node:
                return None
            if node in copied:
                return copied[node]
            copy_node=Node(node.val)
            copied[node]=copy_node
            for nei in node.neighbors:
                neighbour=dfs(nei)
                copy_node.neighbors.append(neighbour)
            return copy_node
        return dfs(node)
            