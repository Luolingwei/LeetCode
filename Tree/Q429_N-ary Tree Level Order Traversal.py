"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        if not root: return []
        level,ans=[root],[]
        while level:
            ans.append([node.val for node in level])
            level=[node for parent in level for node in parent.children]
        return ans