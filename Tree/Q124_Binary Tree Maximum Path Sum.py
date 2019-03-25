# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        def max_end(node):
            if not node:
                return 0
            left = max_end(node.left)
            right = max_end(node.right)
            self.max = max(self.max, left + right + node.val)
            return max(0, max(left, right) + node.val)
        self.max=-float('inf')
        max_end(root)
        return self.max