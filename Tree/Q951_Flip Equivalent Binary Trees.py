# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        if not root1 or not root2:
            return root1==root2
        if root1==root2: return True
        else:
            return root1.val==root2.val and \
                   (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
                    or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))