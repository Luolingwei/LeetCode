# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 iterative
    # def postorderTraversal(self, root):
    #     return [] if not root else self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]

    def postorderTraversal(self, root):
        ans,stack=[],[root]
        while stack:
            node=stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]