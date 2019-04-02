# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive
    # def getHeight(self,root):
    #     height=0
    #     while root:
    #         height+=1
    #         root=root.left
    #     return height
    #
    # def countNodes(self, root):
    #     if not root:
    #         return 0
    #     l,r=self.getHeight(root.left),self.getHeight(root.right)
    #     if l>r:
    #         return self.countNodes(root.left)+pow(2,r)
    #     else:
    #         return self.countNodes(root.right)+pow(2,l)

    # Solution 2 iterative
    def getHeight(self,root):
        height=0
        while root:
            height+=1
            root=root.left
        return height

    def countNodes(self, root):
        count=0
        while root:
            l,r=self.getHeight(root.left),self.getHeight(root.right)
            if l>r:
                count+=pow(2,r)
                root=root.left
            else:
                count+=pow(2,l)
                root=root.right
        return count