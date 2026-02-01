# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathsum=defaultdict(int)
        pathsum[0]=1
        count=0
        def dfs(node, currSum):
            nonlocal count
            if not node:
                return 
            currSum+=node.val
            count+=pathsum[currSum-targetSum]
            pathsum[currSum]+=1
            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum)
            pathsum[currSum]-=1
        dfs(root, 0)
        return count
            
            