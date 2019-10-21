import heapq
class Solution:
    def find(self,origin,points,k):
        queue=[]
        x0,y0=origin[0],origin[1]
        for x,y in points:
            dist=(x-x0)**2+(y-y0)**2
            heapq.heappush(queue,(dist,[x,y]))
        return [heapq.heappop(queue)[1] for _ in range(k)]

a=Solution()
print(a.find([0,0],[[1,1],[2,2],[3,3],[4,4]],2))