
# 记录每条路径当前最大最小值，当路径结束时更新self.ans

class Solution:
    def maxAncestorDiff(self,root):
        self.ans=0
        def dfs(node,curmin,curmax):
            if node:
                curmin=min(curmin,node.val)
                curmax=max(curmax,node.val)
                dfs(node.left,curmin,curmax)
                dfs(node.right,curmin,curmax)
            else:
                self.ans=max(self.ans,curmax-curmin)
        dfs(root,float('inf'),float('-inf'))
        return self.ans