# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        def dfs(node,curS):
            if node:
                curS+=node.val
                if not node.left and not node.right and curS==sum:
                    return True
                if dfs(node.left,curS) or dfs(node.right,curS):
                    return True
            return False
        return dfs(root,0)