# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findMode(self, root):
        count=collections.Counter()
        def preorder(root):
            if root:
                count[root.val]+=1
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        max_val=max(count.values() or [float('inf')])
        return [key for key,value in count.items() if value==max_val]