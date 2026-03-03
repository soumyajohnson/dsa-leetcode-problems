# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        ans=float("inf")
        def dfs(root):
            nonlocal prev, ans
            if not root:
                return
            dfs(root.left)
            if prev is not None:
                ans=min(ans, abs(prev-root.val))
            prev=root.val
            dfs(root.right)
        dfs(root)
        return ans
