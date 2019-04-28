# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 用dfs从上至下求子树的sum, 在dfs的过程中, 所有子树的sum都会被求一边，用dic记录出现频率即可.
class Solution:
    def findFrequentTreeSum(self, root):
        if not  root: return []
        def dfs(root):
            if not root: return 0
            s=root.val+dfs(root.left)+dfs(root.right)
            freqdic[s]=freqdic.get(s,0)+1
            return s
        freqdic={}
        dfs(root)
        maxval=max(freqdic.values())
        return [key for key in freqdic if freqdic[key]==maxval]