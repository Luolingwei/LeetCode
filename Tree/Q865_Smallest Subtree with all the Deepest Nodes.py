# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        def find(root):
            if not root: return 0
            return max(find(root.left), find(root.right)) + 1

        def lowestcommon(root, level, deepest):
            if not root or level == deepest:
                return root
            left = lowestcommon(root.left, level + 1, deepest)
            right = lowestcommon(root.right, level + 1, deepest)
            return root if (left and right) else (left or right)

        deepest = find(root)
        return lowestcommon(root, 1, deepest)