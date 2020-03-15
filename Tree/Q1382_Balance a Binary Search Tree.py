# Definition for a binary tree node.

# 思路: 先inorder取出有序数组，然后从中间分成两半构建balanced BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root):
        def inorder(node):
            if not node: return []
            res=[]
            res+=inorder(node.left)
            res+=[node.val]
            res+=inorder(node.right)
            return res
        def construct(nums):
            if not nums: return None
            mid=len(nums)//2
            node=TreeNode(nums[mid])
            node.left=construct(nums[:mid])
            node.right=construct(nums[mid+1:])
            return node
        return construct(inorder(root))