# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root, limit):
        if not root:
            return root
        if not root.left and not root.right:  # 判断leaf节点
            return root if root.val>=limit else None
        root.left=self.sufficientSubset(root.left,limit-root.val)
        root.right=self.sufficientSubset(root.right,limit-root.val)
        return root if root.left or root.right else None  # 判断非leaf节点是否有符合要求的root-leaf路径