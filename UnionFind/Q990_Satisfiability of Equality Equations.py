# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

# 思路1: 用defaultdict构建各个元素之间的网络关系, 对于不相等的字母, 进行dfs搜索(如果两个都在conn中), 如果能找到两者的连接, 返回False.
# 思路2: Union Find, 用dic构建26个字母的祖先关系, 然后check是否存在不相等的字母祖先相同的情况.

import string
import collections
class Solution:
    # Solution 1 dfs 44 ms
    # def equationsPossible(self, equations):
    #     def dfs(x,y,visited):
    #         if y in conn[x]:
    #             return True
    #         visited.add(x)
    #         for u in conn[x]:
    #             if u not in visited:
    #                 visited.add(u)
    #                 if dfs(u,y,visited):
    #                     return True
    #                 visited.remove(u)
    #         return False
    #
    #     conn=collections.defaultdict(dict)
    #     for i in string.ascii_lowercase:
    #         conn[i][i]=1
    #     for x,symbol,_,y in equations:
    #         if symbol=='=':
    #             conn[x][y]=1
    #             conn[y][x]=1
    #
    #     for x,symbol,_,y in equations:
    #         if symbol=='!' and x in conn and y in conn:
    #             if dfs(x,y,set()): return False
    #     return True

    # Solution 2 union find 44 ms
    def equationsPossible(self, equations):
        # 寻找祖先
        def find(x):
            if uf[x]!=x: return find(uf[x])
            else: return x
        uf={char:char for char in string.ascii_lowercase}
        # 合并祖先
        for x,symbol,_,y in equations:
            if symbol=='=':
                uf[find(x)]=find(y)
        return not any(symbol=='!' and find(x)==find(y) for x,symbol,_,y in equations)

a=Solution()
print(a.equationsPossible(["d!=d"]))
print(a.equationsPossible(["c==c","b==d","x!=z"]))
print(a.equationsPossible(["b==b","b==e","e==c","d!=e"]))
print(a.equationsPossible(["a==b","b==c","c==d",'c==e','b==u','a==i','c!=i']))
print(a.equationsPossible(["a==d","d==a","c!=c","c==d","f==f","f==a"]))
print(a.equationsPossible(["a==b","e==c","b==c","a!=e"]))
print(a.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"]))