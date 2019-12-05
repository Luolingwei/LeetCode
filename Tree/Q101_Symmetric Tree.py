# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive
    # class Solution:
    #     def isSymmetric(self, root):
    #         def check(tree1, tree2):
    #             if not tree1 or not tree2:
    #                 return tree1 == tree2
    #             return tree1.val == tree2.val and check(tree1.left, tree2.right) and check(tree1.right, tree2.left)
    #
    #         if not root:
    #             return True
    #         return check(root.left, root.right)

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