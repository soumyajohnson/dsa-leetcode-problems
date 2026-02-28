# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        inoleft=inorder[:i]
        inoright=inorder[i+1:]
        inoleft_size=len(inoleft)
        preleft=preorder[1:inoleft_size+1]
        preright=preorder[inoleft_size+1:]
        root.left=self.buildTree(preleft,inoleft)
        root.right=self.buildTree(preright,inoright)
        return root