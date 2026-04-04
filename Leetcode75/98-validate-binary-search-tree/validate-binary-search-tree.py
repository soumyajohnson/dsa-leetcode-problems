# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,l,h):
            if not node:
                return True
            if not(l<node.val<h):
                return False
            left=dfs(node.left,l,node.val)
            right=dfs(node.right,node.val,h)
            return left and right
        return dfs(root, float("-inf"),float("inf"))
            