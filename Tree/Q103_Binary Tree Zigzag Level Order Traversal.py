# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 recursive
    # def zig_add(self,node,ans,level):
    #     if node:
    #         if len(ans)<level+1:
    #             ans.append([])
    #         if level%2==0:
    #             ans[level].append(node.val)
    #         else:
    #             ans[level].insert(0,node.val)
    #         self.zig_add(node.left,ans,level+1)
    #         self.zig_add(node.right,ans,level+1)
    #
    # def zigzagLevelOrder(self, root):
    #     ans,level=[],0
    #     self.zig_add(root,ans,level)
    #     return ans

    #Solution 2 iterative
    def zigzagLevelOrder(self, root):
        ans,stack=[],[(root,0)]
        while stack:
            node,level=stack.pop()
            if node:
                if len(ans)<level+1:
                    ans.append([])
                if level%2==0:
                    ans[level].append(node.val)
                else:
                    ans[level].insert(0,node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return ans