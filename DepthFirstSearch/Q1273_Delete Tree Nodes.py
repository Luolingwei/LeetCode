
# 思路: 先建立parent和child的连接关系，然后进行dfs，返回sum和节点数
# sum等于0时，返回0,0

import collections
class Solution:
    def deleteTreeNodes(self, nodes, parent,value):
        sons=collections.defaultdict(set)
        for i,p in enumerate(parent):
            if p>=0: sons[p].add(i)
        def dfs(i):
            curs,curc=value[i],1
            for j in sons[i]:
                childs,childc=dfs(j)
                curs+=childs
                curc+=childc
            return (curs,curc) if curs else (0,0)
        return dfs(0)[1]

a=Solution()
print(a.deleteTreeNodes(7,[-1,0,0,1,2,2,2],[1,-2,4,0,-2,-1,-1]))