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
    def connect(self, root):
        root_copy=root
        dummy=tail=Node(0,None,None,None)
        while root:
            tail.next=root.left
            if tail.next:
                tail=tail.next
            tail.next=root.right
            if tail.next:
                tail=tail.next
            root=root.next
            if not root:
                root=dummy.next
                tail=dummy
        return root_copy