# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        ans,stack=[],[(root,-1)]
        while stack:
            node,level=stack.pop()
            if node:
                if len(ans)<-level:
                    ans.insert(0,[])
                ans[level].append(node.val)
                stack.append((node.right,level-1))
                stack.append((node.left,level-1))
        return ans