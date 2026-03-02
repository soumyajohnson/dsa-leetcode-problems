# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(curr, node):
            if not node:
                return False
            curr+=node.val
            if not node.right and not node.left:
                return curr==targetSum
            return dfs(curr, node.left) or dfs(curr, node.right)
        return dfs(0,root)
