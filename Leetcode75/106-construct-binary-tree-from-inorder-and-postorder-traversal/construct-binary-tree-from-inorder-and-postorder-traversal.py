# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map={val:i for i,val in enumerate(inorder)}
        post_i=len(postorder)-1
        def build(l,r):
            nonlocal post_i
            if l>r:
                return None
            root_val=postorder[post_i]
            post_i-=1
            root=TreeNode(root_val)
            i=idx_map[root_val]
            root.right=build(i+1,r)
            root.left=build(l,i-1)
            return root
        return build(0,len(inorder)-1)