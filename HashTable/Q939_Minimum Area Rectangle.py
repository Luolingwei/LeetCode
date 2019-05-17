# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2

# 思路: 按列对平面上的点进行检索，并对同一列的纵坐标pairs进行存储，如果找到匹配的纵坐标对(y1,y2)，更新最小矩形面积。

import collections
class Solution:

    # Solution 1 brute force O(n^2)
    # def minAreaRect(self, points):
    #     visited,res=set(),float('inf')
    #     for x1,y1 in points:
    #         for x2,y2 in visited:
    #             if (x1,y2) in visited and (x2,y1) in visited:
    #                 res=min(res,abs(x1-x2)*abs(y1-y2))
    #         visited.add((x1,y1))
    #     return res if res!=float('inf') else 0

    # Solultion 2 ~O(n^1.5)
    def minAreaRect(self, points):
        nx=len(set(x for x,y in points))
        ny=len(set(y for x,y in points))
        if nx==len(points) or ny==len(points):
            return 0

        dic=collections.defaultdict(list)
        if nx<ny:
            for x,y in points:
                dic[x].append(y)
        else:
            for x,y in points:
                dic[y].append(x)

        # 上面的代码用来优化一下，减少循环次数
        memory,res={},float('inf')
        for x in sorted(dic.keys()):
            dic[x].sort()
            for i in range(len(dic[x])):
                for j in range(i):
                    y1,y2=dic[x][j],dic[x][i]
                    if (y1,y2) in memory:
                        res=min(res,(x-memory[(y1,y2)])*(y2-y1))
                    memory[(y1,y2)]=x
        return res if res!=float('inf') else 0


a=Solution()
print(a.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(a.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))