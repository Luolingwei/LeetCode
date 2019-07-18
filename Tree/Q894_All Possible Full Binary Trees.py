# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 总节点数量为N, 必须为奇数, 左右两边也必需为奇数, 构建不同的左右子树并加入ans
# 优化: 用dic记录已经构建过的子树集合，如果遇到，不需重新构建.

class Solution:
    def __init__(self):
        self.memo={0:[],1:[TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in self.memo:
            if not N%2:
                return []
            ans,N=[],N-1
            for l in range(1,N,2):
                for left in self.allPossibleFBT(l):
                    for right in self.allPossibleFBT(N-l):
                        root=TreeNode(0)
                        root.left=left
                        root.right=right
                        ans+=[root]
            self.memo[N]=ans
            return ans
        return self.memo[N]