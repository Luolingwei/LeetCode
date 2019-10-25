# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        self.ans=[]
        def dfs(node,path,curS):
            if node:
                curS+=node.val
                path.append(node.val)
                if not node.left and not node.right and curS==sum:
                    self.ans.append(path[:])
                dfs(node.left,path,curS)
                dfs(node.right,path,curS)
                path.pop()
        dfs(root,[],0)
        return self.ans