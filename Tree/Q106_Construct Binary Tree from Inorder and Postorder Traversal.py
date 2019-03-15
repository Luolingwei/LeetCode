# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder[-1])
        left=inorder.index(root.val)
        root.left=self.buildTree(inorder[:left],postorder[:left])
        root.right=self.buildTree(inorder[left+1:],postorder[left:-1])
        return root

a=Solution()
print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))