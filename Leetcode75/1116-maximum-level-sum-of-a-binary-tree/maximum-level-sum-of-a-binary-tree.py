# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_level=1
        max_sum=float("-inf")
        level_num=1
        q=deque([root])
        while q:
            level=len(q)
            currsum=0
            for i in range(level):
                node=q.popleft()
                currsum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if currsum>max_sum:
                max_sum=currsum
                max_level=level_num
            level_num+=1
        return max_level