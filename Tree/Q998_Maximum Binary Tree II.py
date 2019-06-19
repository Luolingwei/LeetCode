# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 为了使新加入的value在最右边，往右找比它小的节点，找到之后把下面的节点全部移到它左边即可

class Solution:
    def insertIntoMaxTree(self, root, val):
        pre,cur=None,root
        while cur and cur.val>val:
            cur,pre=cur.right,cur
        Node=TreeNode(val)
        Node.left=cur
        if pre: pre.right=Node
        return root if pre else Node