# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive
    # def dfs(self, root,path,ans):
    #     if root:
    #         if not root.left and not root.right:
    #             ans.append(path+str(root.val))
    #         self.dfs(root.left,path+str(root.val)+'->',ans)
    #         self.dfs(root.right,path+str(root.val)+'->',ans)
    #
    # def binaryTreePaths(self, root):
    #     ans=[]
    #     self.dfs(root,'',ans)
    #     return ans

    # Solution 2 iterative
    def binaryTreePaths(self, root):
        stack,ans=[(root,'')],[]
        while stack:
            node, path=stack.pop()
            if node:
                if not node.left and not node.right:
                    ans.append(path+str(node.val))
                stack.append((node.left,path+str(node.val)+'->'))
                stack.append((node.right,path+str(node.val)+'->'))
        return ans