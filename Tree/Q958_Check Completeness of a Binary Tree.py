# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 完全二叉树在碰到第一个空节点的时候，后面应该都是空节点, bfs从上到下从左到右加入树的节点.

class Solution:
    def isCompleteTree(self, root):
        queue=[root]
        while queue:
            node=queue.pop(0)
            if not node: return not any(queue)
            queue.append(node.left)
            queue.append(node.right)