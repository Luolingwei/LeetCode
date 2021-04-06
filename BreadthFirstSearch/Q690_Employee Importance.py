
# 思路: 先构建关系图, 然后bfs从start搜索即可

class Solution:
    def getImportance(self, employees, id):
        sub, values = {}, {}
        for e in employees:
            i, v, s = e.id, e.importance, e.subordinates
            values[i] = v
            sub[i] = s
        res = 0
        bfs = [id]
        while bfs:
            new_bfs = []
            for x in bfs:
                res += values[x]
                if x in sub: new_bfs += sub[x]
            bfs = new_bfs
        return res