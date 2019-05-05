"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    # Solution 1: recursive
    # def preorder(self, root):
    #     if not root: return []
    #     ans=[root.val]
    #     for child in root.children:
    #         ans+=self.preorder(child)
    #     return ans


    # Solution 2: iterative
    def preorder(self, root):
        stack,ans=[root],[]
        while stack:
            node=stack.pop()
            if node:
                ans.append(node.val)
                stack+=node.children[::-1]
        return ans