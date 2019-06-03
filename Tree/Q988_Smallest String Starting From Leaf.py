# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root):
        self.ans='}'
        def dfs(root,path):
            if root:
                if not root.left and not root.right:
                    self.ans=min(self.ans,chr(ord('a')+root.val)+path)
                dfs(root.left,chr(ord('a')+root.val)+path)
                dfs(root.right,chr(ord('a')+root.val)+path)
        dfs(root,'')
        return self.ans