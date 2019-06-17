# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 先在inorder中找出根节点的位置，然后先构建左子树，（因为preorder pop的过程中先pop左子树的根节点），再构建右子树

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[idx])
            root.left=self.buildTree(preorder,inorder[:idx])
            root.right=self.buildTree(preorder,inorder[idx+1:])
            return root

a=Solution()
print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))