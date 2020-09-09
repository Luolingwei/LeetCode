
# 思路: union find先构建1和2共同的graph, union未成功的属于多余的
# 然后分别union 1和2 单独的edge, 没union上的属于分别的多余的
# 最后检查1和2 union成功的是否都等于n-1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges):

        def find(x):
            while x != uf[x]:
                while uf[uf[x]] != uf[x]:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        uf = [i for i in range(n + 1)]

        s1, s2 = 0, 0
        res = 0
        for m, x, y in edges:
            if m == 3:
                if not union(x, y):
                    res += 1
                else:
                    s1 += 1
                    s2 += 1

        copy_uf = uf[:]
        for m, x, y in edges:
            if m == 1:
                if not union(x, y):
                    res += 1
                else:
                    s1 += 1

        uf = copy_uf
        for m, x, y in edges:
            if m == 2:
                if not union(x, y):
                    res += 1
                else:
                    s2 += 1

        return res if s1 == s2 == n - 1 else -1

a=Solution()
print(a.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
print(a.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
print(a.maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]]))