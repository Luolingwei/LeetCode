import heapq
class Solution:
    def find(self,origin,points,k):
        if not origin: return []
        queue,ans=[],[]
        x0,y0=origin[0],origin[1]
        for x,y in points:
            dist=(x-x0)**2+(y-y0)**2
            heapq.heappush(queue,(dist,[x,y]))
        for _ in range(k):
            if queue: ans.append(heapq.heappop(queue)[1])
            else: break
        return ans

a=Solution()
print(a.find([0,0],[[1,1],[2,2],[3,3],[4,4]],2))
print(a.find([0,0],[[1,1],[2,2],[3,3],[4,4]],0))
print(a.find([],[[1,1],[2,2],[3,3],[4,4]],0))
print(a.find([0,0],[],2))
print(a.find([0,0],[[1,1],[2,2]],5))