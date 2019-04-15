# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #平衡树的判断条件，左子树和右子树都是平衡树，且左右子树的深度相差不超过1
    def isBalanced(self, root):
        def check(root):
            if not root:
                return (0,True)
            l_depth,l_balance=check(root.left)
            r_depth,r_balance=check(root.right)
            return max(l_depth,r_depth)+1,l_balance and r_balance and abs(l_depth-r_depth)<=1
        return check(root)[1]