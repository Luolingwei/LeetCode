"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root):
        return 0 if not root else max([self.maxDepth(node) for node in root.children] or [0])+1