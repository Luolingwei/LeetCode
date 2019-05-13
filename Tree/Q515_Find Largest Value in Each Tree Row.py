# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        if not root: return []
        ans,level=[],[root]
        while level:
            ans.append(max([node.val for node in level]))
            level=[node for parent in level for node in (parent.left,parent.right) if node]
        return ans