# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,path,ans,target):
        if not root:
            return
        if root and not root.left and not root.right:
            if sum(path)+root.val==target:
                ans.append(path+[root.val])
            return
        else:
            self.dfs(root.left,path+[root.val],ans,target)
            self.dfs(root.right,path+[root.val],ans,target)
    def pathSum(self, root, sum):
        ans=[]
        self.dfs(root,[],ans,sum)
        return ans