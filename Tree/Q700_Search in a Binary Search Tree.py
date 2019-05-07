# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1: recursive
    # def searchBST(self, root, val):
    #     if not root: return []
    #     if val==root.val:
    #         return root
    #     if val>root.val:
    #         return self.searchBST(root.right,val)
    #     if val<root.val:
    #         return self.searchBST(root.left,val)

    # Solution 2: iterative
    def searchBST(self, root, val):
        if not root: return []
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                if val==node.val:
                    return node
                if val<node.val:
                    stack.append(node.left)
                if val>node.val:
                    stack.append(node.right)
        return None