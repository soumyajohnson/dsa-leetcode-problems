# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree=[]
        def dfs(node):
            if not node:
                tree.append('#')
                return
            tree.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(tree)
        return ','.join(tree)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree=data.split(',')
        i=0
        def dfs():
            nonlocal i
            if tree[i]=='#':
                i+=1
                return None
            node=TreeNode(int(tree[i]))
            i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))