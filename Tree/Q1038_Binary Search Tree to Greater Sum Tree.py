# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 右中左遍历，用sum记录已遍历节点的总值，并依次赋给当前节点.

class Solution:
    def __init__(self):
        self.sum=0
    def bstToGst(self, root):
        if not root: return root
        self.bstToGst(root.right)
        self.sum+=root.val
        root.val=self.sum
        self.bstToGst(root.left)
        return root