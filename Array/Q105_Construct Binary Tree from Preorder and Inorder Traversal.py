# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        left = inorder.index(root.val)
        # 建立左子树
        root.left = self.buildTree(preorder[1:left + 1], inorder[:left])
        # 建立右子树
        root.right = self.buildTree(preorder[left + 1:], inorder[left + 1:])

        return root

a=Solution()
print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))