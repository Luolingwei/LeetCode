# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: Solution 1 找左右子树分界点，Solution 2 设置low, high范围

class Solution:
    # Solution 1
    def bstFromPreorder(self, preorder):
        if not preorder: return None
        root=TreeNode(preorder[0])
        i,val=0,preorder[0]
        while i<len(preorder) and preorder[i]<=val:i+=1
        root.left=self.bstFromPreorder(preorder[1:i])
        root.right=self.bstFromPreorder(preorder[i:])
        return root

    # Solution 2
    def bstFromPreorder(self, preorder):
        def build(low,high):
            if preorder and low<preorder[0]<high:
                val=preorder.pop(0)
                root=TreeNode(val)
                root.left=build(low,val)
                root.right=build(val,high)
                return root
        return build(float('-inf'),float('inf'))