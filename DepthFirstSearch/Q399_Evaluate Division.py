# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

# 思路1:用defaultdict构建各个元素之间的网络关系,然后用dfs进行搜索

import collections
class Solution:
    def calcEquation(self, equations, values, queries):
        def dfs(x,y,visited):
            if y in conn[x]:
                return conn[x][y]
            visited.add(x)
            for u,v1 in conn[x].items():
                if u not in visited:
                    visited.add(u)
                    v2=dfs(u,y,visited)
                    if v2!=-1.0:
                        return v1*v2
                    visited.remove(u)
            return -1.0
        conn=collections.defaultdict(dict)
        for (x,y),value in zip(equations,values):
            conn[x][y]=value
            conn[y][x]=1.0/value
            conn[x][x]=1.0
            conn[y][y]=1.0
        return [dfs(x,y,set()) if x in conn and y in conn else -1.0 for x,y in queries]

a=Solution()
print(a.calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
print(a.calcEquation([ ["a", "b"], ["f", "g"] ],[2.0, 3.0],[ ["a", "g"]]))