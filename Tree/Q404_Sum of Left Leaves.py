# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        total=0
        if root.left:
            if not root.left.left and not root.left.right:
                total+=root.left.val
            else:
                total+=self.sumOfLeftLeaves(root.left)
        if root.right:
            total+=self.sumOfLeftLeaves(root.right)
        return total