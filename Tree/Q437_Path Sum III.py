# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 从上至下遍历左右子树，用dic记录以root节点开始，到该节点的所有路径可能的pathsum的个数(不包含该节点),则在此节点增加的路径数量为dic[pathsum-target],如 dic[10-5-3 - 8]即求从root节点到当前节点pathsum=10的个数

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


class Solution:
    def pathSum(self, root, sum):
        self.ans=0
        memo={0:1}
        def dfs(node,curS):
            if node:
                curS+=node.val
                self.ans+=memo.get(curS-sum,0)
                memo[curS]=memo.get(curS,0)+1
                dfs(node.left,curS)
                dfs(node.right,curS)
                memo[curS]-=1  #root节点已遍历完毕，将转移到root节点的右边相邻节点进行遍历，所以要清除该root节点的pathsum
        dfs(root,0)
        return self.ans