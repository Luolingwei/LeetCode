# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        def dfs(root,path,curSum):
            if root:
                if not root.left and not root.right:
                    if curSum+root.val==sum:
                        ans.append(path+[root.val])
                else:
                    dfs(root.left,path+[root.val],curSum+root.val)
                    dfs(root.right,path+[root.val],curSum+root.val)
        ans=[]
        dfs(root,[],0)
        return ans