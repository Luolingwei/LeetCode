
# 思路: dfs搜索当前node开始的最长increase路径和最长decrease路径, res = max(res, desc+incr-1)
# T(n) = 2*T(n/2) + O(1)
# a = 2, b = 2, c = 0, T(n) = O(n)

class Solution:
    def longestConsecutive(self, root):
        self.res = 0
        def dfs(node):
            if not node: return 0,0
            descL, incrL = dfs(node.left)
            descR, incrR = dfs(node.right)
            desc, incr = 1, 1
            if node.left:
                if node.val==node.left.val+1:
                    desc = max(desc, descL + 1)
                elif node.val==node.left.val-1:
                    incr = max(incr, incrL + 1)
            if node.right:
                if node.val==node.right.val+1:
                    desc = max(desc, descR + 1)
                elif node.val==node.right.val-1:
                    incr = max(incr, incrR + 1)
            self.res = max(self.res, desc+incr-1)
            return desc, incr
        dfs(root)
        return self.res