# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

# Input: pre=[2,1]，post=[1,2]
# Output: [2,1]

# 根据第二个数，即左子树的根节点来划分左右子树的元素

class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root=TreeNode(pre.pop(0))
        post.pop()
        if pre:
            idx=post.index(pre[0])
            root.left=self.constructFromPrePost(pre[:idx+1],post[:idx+1])
            root.right=self.constructFromPrePost(pre[idx+1:],post[idx+1:])
        return root