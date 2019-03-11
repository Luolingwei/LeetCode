# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node):
        if not node:
            return 0,0
        y1,n1=self.helper(node.left)
        y2,n2=self.helper(node.right)
        return max(node.val+n1+n2,y1+y2),y1+y2
    def rob(self, root):
        return self.helper(root)[0]