from collections import defaultdict

# 思路: union find, 对target能交换的所有Index连成一片, 他们之间可以随意排列, 统计每一片所有的数字个数
# 对每个source里的数字寻找其所属的片区(find(x)), 如果片区中还剩下有该数字, 个数减1, 否则无法匹配, res+1

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
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

        N = len(source)
        uf = {}
        for u, v in allowedSwaps:
            union(u, v)

        memo = defaultdict(lambda: defaultdict(int))
        res = 0
        for i in range(N):
            memo[find(i)][target[i]] += 1
        for i in range(N):
            if memo[find(i)][source[i]] > 0:
                memo[find(i)][source[i]] -= 1
            else:
                res += 1
        return res


a=Solution()
print(a.minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]))
print(a.minimumHammingDistance([1,2,3,4], [1,3,2,4], []))
print(a.minimumHammingDistance([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]))