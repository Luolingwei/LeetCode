
# dfs bottom-up返回status,min,max,count，碰到status为true时，用count更新ans
# 判断bst: 左右都是bst而且lmax<node.val<rmin

class Solution:
    def largestBSTSubtree(self, root):
        self.ans=0
        def dfs(node):
            if not node: return True,float('inf'),float('-inf'),0
            lstatus,lmin,lmax,lcount=dfs(node.left)
            rstatus,rmin,rmax,rcount=dfs(node.right)
            cstatus=lstatus and rstatus and lmax<node.val<rmin
            cmin,cmax=min(node.val,lmin,rmin),max(node.val,lmax,rmax)
            ccount=lcount+rcount+1
            if cstatus and ccount>self.ans:
                self.ans=ccount
            return cstatus,cmin,cmax,ccount
        dfs(root)
        return self.ans