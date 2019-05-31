# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1: iterative
    # def addOneRow(self, root, v, d):
    #     stack=[(root,1)]
    #     if d==1:
    #         new_root=TreeNode(v)
    #         new_root.left=root
    #         return new_root
    #     while stack:
    #         node,level=stack.pop()
    #         if node:
    #             if level==d-1:
    #                 preL,preR=node.left,node.right
    #                 node.left,node.right=TreeNode(v),TreeNode(v)
    #                 node.left.left,node.right.right=preL,preR
    #             else:
    #                 stack.append((node.left,level+1))
    #                 stack.append((node.right,level+1))
    #     return root

    # Solution 2: level by level
    def addOneRow(self, root, v, d):
        depth,level=1,[root]
        if d==1:
            new_root=TreeNode(v)
            new_root.left=root
            return new_root
        while depth<d-1:
            level=[node for parent in level for node in (parent.left,parent.right) if node]
            depth+=1
        for node in level:
            preL,preR=node.left,node.right
            node.left,node.right=TreeNode(v),TreeNode(v)
            node.left.left,node.right.right=preL,preR
        return root