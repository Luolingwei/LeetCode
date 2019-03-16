"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # solution 1 iterative
    # def connect(self, root):
    #     ans=root
    #     while root and root.left:
    #         next=root.left
    #         while root:
    #             root.left.next=root.right
    #             root.right.next=root.next and root.next.left
    #             root=root.next
    #         root=next
    #     return ans

    #solution 2 recursive
    def connect(self, root):
        if root and root.left:
            root.left.next=root.right
            root.right.next=root.next and root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root