# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        temp=root.left
        if temp:
            while temp and temp.right:
                temp=temp.right
            temp.right=root.right
            root.right=root.left
            root.left=None