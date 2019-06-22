# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: dfs root.left,root.right得到给parent的coins数量, root需要给出去的数量为left+right+root.val-1

class Solution:
    def distributeCoins(self, root):
        self.moves=0
        def dfs(root):
            if not root: return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.moves+=abs(left)+abs(right)
            return root.val+left+right-1
        dfs(root)
        return self.moves