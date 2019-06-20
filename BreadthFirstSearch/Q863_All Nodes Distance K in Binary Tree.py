# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路:先用一个map存储所有节点的连接关系，然后进行bfs

import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        conn=collections.defaultdict(list)
        def connect(parent,child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child,child.left)
            if child.right: connect(child,child.right)
        connect(None,root)

        bfs,visited,dist=[target.val],{target.val},0
        for _ in range(K):
            bfs=[node for old in bfs for node in conn[old] if node not in visited]
            visited|=set(bfs)
        return bfs