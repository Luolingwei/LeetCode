import bisect
class Solution:
    def shortestDistanceColor(self, colors, queries):
        idxs = [[] for _ in range(3)]
        for i,c in enumerate(colors):
            idxs[c-1].append(i)
        res = [-1]*len(queries)
        for i in range(len(queries)):
            pos, color = queries[i][0], queries[i][1]
            dist = float('inf')
            larger_i = bisect.bisect_left(idxs[color-1],pos)
            if larger_i<len(idxs[color-1]):
                dist = min(dist,idxs[color-1][larger_i] - pos)
            if larger_i>0:
                smaller_i = larger_i-1
                dist = min(dist,pos - idxs[color-1][smaller_i])
            if dist!=float('inf'): res[i] = dist
        return res


a=Solution()
print(a.shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]))
print(a.shortestDistanceColor([1,2], [[0,3]]))