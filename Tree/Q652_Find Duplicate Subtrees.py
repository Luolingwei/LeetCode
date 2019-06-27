# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 将各个子树转成string表示的形式，存到字典中.返回有重复string的value.

import collections
class Solution:
    def findDuplicateSubtrees(self, root):
        dic=collections.defaultdict(list)
        def inorder(root):
            if not root:return '#'
            strings=str(root.val)+inorder(root.left)+inorder(root.right)
            dic[strings].append(root)
            return strings
        inorder(root)
        return [nodes[0] for nodes in dic.values() if len(nodes)>1]