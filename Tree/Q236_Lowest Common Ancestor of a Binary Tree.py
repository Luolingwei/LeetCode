# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution, but TLE
    # def helper(self,root,node):
    #     if not root:
    #         return False
    #     if root==node:
    #         return True
    #     else:
    #         return self.helper(root.left,node) or self.helper(root.right,node)
    # def lowestCommonAncestor(self, root, p, q):
    #     while True:
    #         if self.helper(root.left,p) and self.helper(root.left,q):
    #             root=root.left
    #         elif self.helper(root.right,p) and self.helper(root.right,q):
    #             root=root.right
    #         else:
    #             return root

    # amazing solution
    def lowestCommonAncestor(self, root, p, q):
        if root in (p,q,None): return root
        left,right=self.lowestCommonAncestor(root.left,p,q),self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        else: return left or right