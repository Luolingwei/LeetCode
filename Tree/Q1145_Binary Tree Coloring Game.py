# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 对于一个x，second player能cover的范围有3种，x.left,x.right,x.parent
# 用dfs count进行计算，left=count(x.left),right=count(x.right),parent=n-left-right-1
# 如果这三种的最大值大于n//2，则可以获胜

class Solution:
    def btreeGameWinningMove(self, root, n, x):
        memo=[0,0]
        def count(node):
            if not node: return 0
            l,r=count(node.left),count(node.right)
            if node.val==x:
                memo[0],memo[1]=l,r
            return l+r+1
        count(root)
        return max(max(memo),n-sum(memo)-1)>n//2