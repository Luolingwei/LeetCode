# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        level=[root]
        while level:
            leftmost=level[0]
            level=[node for parent in level for node in (parent.left,parent.right) if node]
        return leftmost