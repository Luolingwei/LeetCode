# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

# 思路: Union Find, 用dic构建26个字母的祖先关系, 然后check是否存在不相等的字母祖先相同的情况.

import string
class Solution:
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
print(a.equationsPossible(["c==c","b==d","x!=z"]))
print(a.equationsPossible(["b==b","b==e","e==c","d!=e"]))
print(a.equationsPossible(["a==b","b==c","c==d",'c==e','b==u','a==i','c!=i']))
print(a.equationsPossible(["a==d","d==a","c!=c","c==d","f==f","f==a"]))
print(a.equationsPossible(["a==b","e==c","b==c","a!=e"]))
print(a.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"]))