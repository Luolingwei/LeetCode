# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 iterative
    # def preorderTraversal(self, root):
    #     return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    # Solution 2 iterative
    def preorderTraversal(self, root):
        stack,ans=[root],[]
        while stack:
            node=stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans