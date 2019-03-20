# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,n,sum):
        if not root:
            return False
        if root and not root.left and not root.right:
            return n+root.val==sum
        else:
            return self.dfs(root.left,n+root.val,sum) or self.dfs(root.right,n+root.val,sum)
    def hasPathSum(self, root,sum):
        return self.dfs(root,0,sum)