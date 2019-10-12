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

# 对于post，左右中，3一定是右子树的根节点，在pre中找，区分左右子树，同理，2一定是左子树的根节点，在post中找，区分左右子树
# 默认左右子树都存在，只存在一个要单独考虑，会导致左右子树区分反，程序出错
# 只存在一个left或right时，仍然有pre[0]=post[last]，此时将子树置为左子树或右子树都ok

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