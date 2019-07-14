# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 如果节点属于底层节点，返回该节点，若为空返回空
# 当左右都有返回时，返回root，否则返回left or right.

class Solution:
    def lcaDeepestLeaves(self, root):
        def find_depth(root):
            return -1 if not root else max(find_depth(root.left),find_depth(root.right))+1
        max_deep=find_depth(root)
        def dfs(root,level):
            if level==max_deep or not root: return root
            left,right=dfs(root.left,level+1),dfs(root.right,level+1)
            if left and right: return root
            else: return left or right
        return dfs(root,0)