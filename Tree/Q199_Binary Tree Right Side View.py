# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #solution 1 recursive
    # def rightSideView(self, root):
    #     if not root: return []
    #     left=self.rightSideView(root.left)
    #     right=self.rightSideView(root.right)
    #     return [root.val]+right+left[len(right):]

    #solution 2 iterative
    def rightSideView(self, root):
        view,level=[],[root]
        while root and level:
            view.append(level[-1].val)
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return view