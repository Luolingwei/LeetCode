
# 思路: 对所有pair按距离，人和车的index进行排序，然后扫一遍，如果人和车都还未使用就assign

class Solution:
    def assignBikes(self, workers, bikes):
        def helper(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        q=[]
        ans=[-1]*len(workers)
        visitedW,visitedB=set(),set()
        for wi,w in enumerate(workers):
            for bi,b in enumerate(bikes):
                q.append((helper(w,b),wi,bi))
        for d,wi,bi in sorted(q):
            if wi not in visitedW and bi not in visitedB:
                ans[wi]=bi
                visitedW.add(wi)
                visitedB.add(bi)
        return ans

a=Solution()
print(a.assignBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]))