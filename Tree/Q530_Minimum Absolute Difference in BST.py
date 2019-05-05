# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 由于中序遍历BST得到的数组值是递增的，所以中序遍历取出所有值之后找出数组中的最大gap即可

class Solution:
    def getMinimumDifference(self, root):
        nums=[]
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        inorder(root)
        return min([nums[i+1]-nums[i] for i in range(len(nums)-1)])