# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node,path):
        if not node:
            return
        if node and not any((node.left,node.right)):
            self.ans=self.ans+path*10+node.val
        self.helper(node.left,path*10+node.val)
        self.helper(node.right,path*10+node.val)
    def sumNumbers(self, root):
        self.ans=0
        self.helper(root,0)
        return self.ans