# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 inorder
    # def inorder(self,root,nodes):
    #     if root:
    #         self.inorder(root.left,nodes)
    #         nodes.append(root.val)
    #         self.inorder(root.right,nodes)
    #
    # def kthSmallest(self, root,k):
    #     nodes=[]
    #     self.inorder(root,nodes)
    #     return nodes[k-1]

    # Solution 2 iterative
    def kthSmallest(self,root,k):
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right