# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 用S,L分别记录各条路径的最大值和最小值，并更新最大gap(L-S)

class Solution:
    def maxAncestorDiff(self, root):
        self.max=0
        def dfs(node,S,L):
            if node:
                S,L=min(S,node.val),max(L,node.val)
                self.max=max(self.max,L-S)
                dfs(node.left,S,L)
                dfs(node.right,S,L)
        dfs(root,float('inf'),float('-inf'))
        return self.max