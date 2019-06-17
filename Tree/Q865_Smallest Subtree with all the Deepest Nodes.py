# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        def get_deepest(root):
            level,pre=[root],[]
            while level:
                pre=level
                level=[node for parent in level for node in (parent.left,parent.right) if node]
            return pre
        def get_root(deepest,root):
            if root in deepest: return root
            left,right=get_root(deepest,root.left),get_root(deepest,root.right)
            if left and right: return root
            else: return left or right
        deepest=set(get_deepest(root)+[None])
        return get_root(deepest,root)