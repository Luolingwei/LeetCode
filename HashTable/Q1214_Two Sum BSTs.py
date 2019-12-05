# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1, root2, target):
        def inorder(root):
            res=[]
            if not root:
                return []
            res+=inorder(root.left)
            res+=[root.val]
            res+=inorder(root.right)
            return res
        nums1=set(inorder(root1))
        nums2=inorder(root2)
        for n in nums2:
            if target-n in nums1:
                return True
        return False