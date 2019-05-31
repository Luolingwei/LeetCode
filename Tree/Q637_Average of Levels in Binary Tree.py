# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        ans,level=[],[root]
        while level:
            ans+=[sum(node.val for node in level)/len(level)]
            level=[node for parent in level for node in (parent.left,parent.right) if node]
        return ans