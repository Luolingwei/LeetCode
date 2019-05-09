# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        if not root: return TreeNode(val)
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left,val)
        return root