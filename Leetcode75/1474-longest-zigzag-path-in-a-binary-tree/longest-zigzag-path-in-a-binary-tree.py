# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        count=0
        def dfs(node,left,l):
            nonlocal count
            if not node:
                return 
            l+=1
            count=max(count,l)
            if left:
                dfs(node.right,False,l)
                dfs(node.left, True,0)
            else:
                dfs(node.left,True,l)
                dfs(node.right,False,0)
        dfs(root.left, True,0)
        dfs(root.right,False,0)
        return count
            