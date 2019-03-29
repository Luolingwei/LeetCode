# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive
    # def helper(self,l,r):
    #     if l and r:
    #         return l.val==r.val and self.helper(l.left,r.right) and self.helper(l.right,r.left)
    #     else:
    #         return l==r
    #
    # def isSymmetric(self, root):
    #     if not root:
    #         return True
    #     return self.helper(root.left,root.right)

   # Solution 2 iterative
    def isSymmetric(self, root):
        if not root:
            return True
        stack=[(root.left,root.right)]
        while stack:
            l,r=stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val!=r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True