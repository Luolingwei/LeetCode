# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

class Solution:
    # Solution 1 recursive
    # def rangeSumBST(self, root, L, R):
    #     ans=0
    #     if not root: return 0
    #     if L<=root.val<=R:
    #         ans+=root.val
    #     if root.val>L:
    #         ans+=self.rangeSumBST(root.left,L,R)
    #     if root.val<R:
    #         ans+=self.rangeSumBST(root.right,L,R)
    #     return ans

    # Solution 2 iterative
    def rangeSumBST(self, root, L, R):
        stack,ans=[root],0
        while stack:
            node=stack.pop()
            if node:
                if L<=node.val<=R:
                    ans+=node.val
                if node.val>L:
                    stack.append(node.left)
                if node.val<R:
                    stack.append(node.right)
        return ans