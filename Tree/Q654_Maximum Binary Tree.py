# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1

# 思路: 先找出max的位置，然后递归解决左右子树

class Solution:
    # Solution 1 recursive
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        max_value=max(nums)
        idx=nums.index(max_value)
        root=TreeNode(max_value)
        root.left=self.constructMaximumBinaryTree(nums[:idx])
        root.right=self.constructMaximumBinaryTree(nums[idx+1:])
        return root