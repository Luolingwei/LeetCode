# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路:先在inorder中找出根节点的位置，然后先构建右子树，（因为postorder pop的过程中先pop右子树的根节点），再构建左子树

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx=inorder.index(postorder.pop())
            root=TreeNode(inorder[idx])
            root.right=self.buildTree(inorder[idx+1:],postorder)
            root.left=self.buildTree(inorder[:idx],postorder)
            return root

a=Solution()
print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))