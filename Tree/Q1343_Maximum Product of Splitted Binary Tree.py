
# 思路: dfs求每个node下的curs，用(sum-curs)*curs进行更新，第一轮dfs求sum，第二轮dfs进行更新

class Solution:
    def maxProduct(self, root):
        def dfs(node):
            res = 0
            if not node: return 0
            res += node.val
            res += dfs(node.left)
            res += dfs(node.right)
            self.ans = max(self.ans, res*(s-res))
            return res
        s=self.ans=0
        s=dfs(root)
        dfs(root)
        return self.ans%(10**9+7)