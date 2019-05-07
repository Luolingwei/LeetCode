# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 如果某节点是要删除的节点，那么将其右边的分支全部挂到左边的最右路径下（左边不为空），这样可以保证BST的条件，即所有右边的节点都比根节点大。如果左边为空，在右边删除根节点即可。

class Solution:
    def deleteNode(self, root, key):
        if not root: return root
        if root.val==key:
            left,right=root.left,root.right
            if root.left:
                root=p=left
                while p.right:
                    p=p.right
                p.right=right
            else:
                root=right
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        return root