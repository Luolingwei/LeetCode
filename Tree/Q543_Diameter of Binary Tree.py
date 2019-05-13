# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 用max_end函数求以各个节点为头节点的最长路径(节点数)，在这个过程中，计算以各个节点为root节点的最长路径(left+right+1)，更新self.max，最终得到最长路径。（最长路径一定以某一个节点为根节点）

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans=1
        def max_end(root):
            if not root:return 0
            left=max_end(root.left)
            right=max_end(root.right)
            self.ans=max(self.ans,left+right+1)
            return max(left,right)+1
        max_end(root)
        return self.ans-1