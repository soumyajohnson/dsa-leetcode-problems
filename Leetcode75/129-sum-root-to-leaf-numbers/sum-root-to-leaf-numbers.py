# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(total,node):
            if not node:
                return 0
            total=total*10+node.val
            if not node.right and not node.left:
                return total
            return dfs(total,node.left)+dfs(total, node.right)
        return dfs(0,root)
            