# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

# 思路: 以postorder根节点前一个点作为分界的标志，区分左右子树的节点，post(左右中),pre(中左右),所以post最后的节点会在pre中最前面出现

class Solution:
    def constructFromPrePost(self, pre, post):
        if pre:
            root=TreeNode(post.pop())
            pre.pop(0)
            if pre:
                if pre[0]==post[-1]:
                    root.left=self.constructFromPrePost(pre,post)
                else:
                    l,r=pre.index(post[-1]),post.index(pre[0])
                    root.left=self.constructFromPrePost(pre[:l],post[:r+1])
                    root.right=self.constructFromPrePost(pre[l:],post[r+1:])
            return root