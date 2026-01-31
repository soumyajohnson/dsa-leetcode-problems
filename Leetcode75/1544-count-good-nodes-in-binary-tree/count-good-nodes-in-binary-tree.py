# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxval):
            if not root:
                return 0
            count=0
            if root.val>=maxval:
                count=1
                maxval=max(root.val,maxval)
            count+=dfs(root.left, maxval)
            count+=dfs(root.right, maxval)
            return count
        return dfs(root, root.val)

            