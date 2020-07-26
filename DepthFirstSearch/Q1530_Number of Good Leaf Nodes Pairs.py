from collections import Counter

# 思路: dfs从叶子节点返回, Counter统计当前节点下的叶子节点距离分布情况
# 在每一个节点将左右叶子节点进行配对, 并汇总左右叶子节点距离分布返回(dist+1)

class Solution:
    def countPairs(self, root, distance):
        self.res = 0
        def dfs(node):
            if not node: return Counter()
            if not node.left and not node.right:
                return Counter([0])
            lcount = dfs(node.left)
            rcount = dfs(node.right)
            for ld,ln in lcount.items():
                for rd,rn in rcount.items():
                    if ld+rd+2<=distance: self.res += ln*rn
            return Counter({k+1:v for k,v in (lcount+rcount).items()})
        dfs(root)
        return self.res