
# 将每个喷泉的范围用区间存储，每个left只存储最大的right，先开启第一个喷泉，然后计算此end+1内的最大end，更新end，ans+1(开启另外一个喷泉)，直到end到达末尾

import collections
class Solution:
    def activate(self,limits):
        L=len(limits)
        intervals=collections.defaultdict(int)
        for i in range(L):
            l,r=max(0,i-limits[i]),min(L-1,i+limits[i])
            intervals[l]=max(intervals[l],r)
        intervals=sorted([(l,intervals[l]) for l in intervals])
        cur,end,ans=0,intervals[0][1],1
        while end<L-1:
            curMax=0
            while cur<len(intervals) and intervals[cur][0]<=end+1:
                curMax=max(curMax,intervals[cur][1])
                cur+=1
            end=curMax
            ans+=1
        return ans

a=Solution()
print(a.activate([1,2,1]))
print(a.activate([0,0,0,3,0,0,2,0,0]))
print(a.activate([3,0,2,0,1,0]))
print(a.activate([3,0,1,0,1,0]))
print(a.activate([3,0,1,0,0,1]))
print(a.activate([2,0,2,0,1,0]))
print(a.activate([2,0,0,0,0]))
print(a.activate([0,0,0,0,0]))
print(a.activate([1,2,1]))
print(a.activate([0,1,0]))