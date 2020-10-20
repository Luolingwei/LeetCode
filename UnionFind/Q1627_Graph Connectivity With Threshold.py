
# 思路: 根据base从1到n, 将base和数字连起来, 如果两个数有大于threshold的公因子, 则他们一定会都和这个base相连
# 只考虑base>threshold, union之后find每一个query即可

class Solution:
    def areConnected(self, n: int, threshold: int, queries):
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

        if not threshold: return [True]*len(queries)
        uf = {}
        for x in range(1, n + 1):
            for y in range(2 * x, n + 1, x):
                if x > threshold:
                    union(x, y)

        return [find(x) == find(y) for x, y in queries]


a=Solution()
print(a.areConnected(6,2,[[1,4],[2,5],[3,6]]))
print(a.areConnected(6,0,[[4,5],[3,4],[3,2],[2,6],[1,3]]))
print(a.areConnected(5,1,[[4,5],[4,5],[3,2],[2,3],[3,4]]))