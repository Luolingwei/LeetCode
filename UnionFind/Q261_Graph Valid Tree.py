
# 思路: 构成树的条件是没有环路, 而且所有node连成1块, 即edge的数量是n-1
# union-find寻找无向图的环

class Solution:
    def validTree(self, n, edges):
        def find(x):
            while x in uf:
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        if len(edges) != n - 1:
            return False
        uf = {}
        for i, j in edges:
            if not union(i, j):
                return False
        return True


a=Solution()
print(a.validTree(5,[[0,1], [0,2], [0,3], [1,4]]))
print(a.validTree(5,[[0,1], [1,2], [2,3], [1,3], [1,4]]))