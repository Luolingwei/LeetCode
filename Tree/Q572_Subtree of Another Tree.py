# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sametree(self,tree1,tree2):
        if not tree1 or not tree2:
            return tree1==tree2
        if tree1.val!=tree2.val:
            return False
        return self.sametree(tree1.left,tree2.left) and self.sametree(tree1.right,tree2.right)

    def isSubtree(self, s, t):
        if not s:
            return False
        return self.sametree(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)