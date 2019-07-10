# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 对root1进行改造，如果有一个为空，则返回root1 or root2，否则，两者的val加起来赋值给root1. 最后返回root1.

class Solution:
    def mergeTrees(self, t1, t2):
        def dfs(root1,root2):
            if not root1 or not root2:
                return root1 or root2
            root1.val+= root2.val
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1
        return dfs(t1,t2)