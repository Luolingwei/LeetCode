# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generate(self,start,end):
        trees=[]
        for root in range(start,end+1):
            for left in self.generate(start,root-1):
                for right in self.generate(root+1,end):
                    node=TreeNode(root)
                    node.left=left
                    node.right=right
                    trees+=node,
        return trees or [None]
    def generateTrees(self, n):
        if not n: return []
        return self.generate(1,n)


