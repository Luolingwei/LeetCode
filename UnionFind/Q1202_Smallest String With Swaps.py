# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"

# pairs可以构成多个多个单独的图，每个联通的子图之间可以无限次交换，所以将子图排序然后合并得到s即可
# 注意这里union find的不同之处，在find时，直接修改u[x]为祖先，简化寻找路径

import collections
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        def union(x,y):
            headx,heady=find(x),find(y)
            if headx!=heady:
                u[heady]=headx

        def find(x): #直接修改u[x]为祖先，简化路径
            if u[x]!=x:
                u[x]=find(u[x])
            return u[x]

        N=len(s)
        u=[i for i in range(N)]
        for x,y in pairs: union(x,y)

        strs,ans=['' for _ in range(N)],['' for _ in range(N)]
        for i in range(N):
            strs[find(i)]+=s[i]
        strs=[sorted(s) for s in strs]

        idx=collections.Counter()
        for i in range(N):
            head=find(i)
            ans[i]=strs[head][idx[head]]
            idx[head]+=1
        return ''.join(ans)

a=Solution()
print(a.smallestStringWithSwaps("dcab",[[0,3],[1,2],[0,2]]))
print(a.smallestStringWithSwaps("dcab",[[0,3],[1,2]]))
print(a.smallestStringWithSwaps("cba",[[0,1],[1,2]]))