# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 recursive
    # def helper(self,root,ans,level):
    #     if root:
    #         if len(ans)<level+1:
    #             ans.append([])
    #         ans[level].append(root.val)
    #         self.helper(root.left,ans,level+1)
    #         self.helper(root.right,ans,level+1)
    # def levelOrder(self, root):
    #     ans=[]
    #     self.helper(root,ans,0)
    #     return ans

    # solution 2 level by level
    # def levelOrder(self, root):
    #     ans,level=[],[root]
    #     while root and level:
    #         ans.append([node.val for node in level])
    #         level=[node for root in level for node in (root.left, root.right) if node]
    #     return ans

    # solution 3 iterative
    def levelOrder(self, root):
        ans,stack=[],[(root,0)]
        while stack:
            node,level=stack.pop()
            if node:
                if len(ans)<level+1:
                    ans.append([])
                ans[level].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return ans