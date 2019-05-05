"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    # Solution 1: recursive
    # def postorder(self, root):
    #     def helper(root):
    #         if not root: return []
    #         ans = [root.val]
    #         for child in root.children[::-1]:
    #             ans+=helper(child)
    #         return ans
    #     return helper(root)[::-1]


    # Solution 2: iterative
    def postorder(self, root):
        stack,ans=[root],[]
        while stack:
            node=stack.pop()
            if node:
                ans.append(node.val)
                stack+=node.children
        return ans[::-1]