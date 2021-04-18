
# 思路: uf, uf成功的次数等于N-1时, 表示所有人都被连起来了

class Solution:
    def earliestAcq(self, logs, N) -> int:
        uf = list(range(N))
        logs.sort(key=lambda x: x[0])

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        connected = 0
        for t, x, y in logs:
            if union(x, y):
                connected += 1
                if connected == N - 1:
                    return t
        return -1


a=Solution()
print(a.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6))