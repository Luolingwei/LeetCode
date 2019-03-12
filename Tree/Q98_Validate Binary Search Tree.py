# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root,ans):
        if not root:
            return
        else:
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
        return ans
    def isValidBST(self, root):
        ans=[]
        self.inorder(root,ans)
        return sorted(list(set(ans)))==ans