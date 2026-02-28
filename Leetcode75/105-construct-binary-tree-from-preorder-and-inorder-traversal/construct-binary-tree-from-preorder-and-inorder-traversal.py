# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map={val:i for i,val in enumerate(inorder)}
        pre_i=0
        def build(l,r):
            nonlocal pre_i
            if l>r:
                return None
            root_val=preorder[pre_i]
            pre_i+=1
            root=TreeNode(root_val)
            i=idx_map[root_val]
            root.left=build(l,i-1)
            root.right=build(i+1,r)
            return root
        return build(0,len(inorder)-1)