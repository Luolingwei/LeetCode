# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路1: 设置一个全局index，记录目前访问到的节点数，index=1时，返回当前访问节点，即第k小的数

class Solution:
    # Solution 1 recursive
    # def kthSmallest(self,root,k):
    #     self.idx = k
    #     self.ans = 0
    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             if self.idx == 1:
    #                 self.ans = node.val
    #                 return
    #             self.idx -= 1
    #             inorder(node.right)
    #     inorder(root)
    #     return self.ans

    # Solution 2 iterative
    def kthSmallest(self,root,k):
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right