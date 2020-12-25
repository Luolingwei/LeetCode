
# 思路: union find, 将query按limit从小到大sort, 每次加入小于当前limit的所有edge, union起来
# 根据当前的图find(x,y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
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

        edgeList.sort(key=lambda x: x[2])

        i = 0
        res, uf = [False] * len(queries), {}
        for limit, x, y, idx in sorted((q[2], q[0], q[1], i) for i, q in enumerate(queries)):
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[idx] = (find(x) == find(y))
        return res


a=Solution()
print(a.distanceLimitedPathsExist(3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]]))
print(a.distanceLimitedPathsExist(5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]]))