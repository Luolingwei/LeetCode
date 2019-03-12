# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 recursive
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

    # solution 2 iterative
    def maxDepth(self, root):
        stack,res=[(root,0)],0
        while stack:
            node,level=stack.pop()
            if not node:
                res=max(res,level)
            else:
                stack.append((node.left,level+1))
                stack.append((node.right,level+1))
        return res