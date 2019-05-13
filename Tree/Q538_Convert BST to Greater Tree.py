# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# 由于是累加比当前节点大的值，所以不能先访问左边的节点，因为右边的节点值还没有存储。故以dfs先访问右边节点，将节点值累加起来，然后访问左边节点的时候就有右边所有节点值的sum了.（遍历顺序，右中左）

class Solution:
    def __init__(self):
        self.sum=0
    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.sum+=root.val
            root.val=self.sum
            self.convertBST(root.left)
        return root