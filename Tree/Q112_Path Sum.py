# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root,sum):
        def dfs(root,curSum):
            if root:
                if not root.left and not root.right:
                    if curSum+root.val==sum: return True
                else:
                    return dfs(root.left,curSum+root.val) or dfs(root.right,curSum+root.val)
        return bool(dfs(root,0))